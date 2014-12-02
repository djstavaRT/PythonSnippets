__author__ = 'djstava'

import sys
from PyQt4 import QtGui,QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(800,600)
        self.setWindowTitle("AutoTestKit")

        self.statusBar().showMessage("Ready")

        '''
        p = QtGui.QPalette()
        brush = QtGui.QBrush(QtCore.Qt.white,QtGui.QPixmap('logo.jpg'))
        p.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Window,brush)
        #p.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,brush)
        #p.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Window,brush)
        self.setPalette(p)
        '''

        layout = QtGui.QVBoxLayout()
        djTextEdit = QtGui.QTextEdit()
        layout.addWidget(djTextEdit)
        djTextEdit.append('Welcome to autoTestKit')

        menuBar = self.menuBar()

        proj_menu = menuBar.addMenu('&Projects')
        app = QtGui.QAction('App',self)
        app.setShortcut('Ctrl+A')
        app.setStatusTip('Test app')
        self.connect(app,QtCore.SIGNAL('triggered()'),self.slotOnClickApp)

        iploader = QtGui.QAction('Iploader',self)
        iploader.setShortcut('Ctrl+I')
        iploader.setStatusTip('Test iploader')
        self.connect(iploader,QtCore.SIGNAL('triggered()'),self.slotOnClickIploader)

        otaloader = QtGui.QAction('Otaloader',self)
        otaloader.setShortcut('Ctrl+I')
        otaloader.setStatusTip('Test otaloader')
        self.connect(otaloader,QtCore.SIGNAL('triggered()'),self.slotOnClickOtaloader)

        exit = QtGui.QAction('Exit',self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit')
        self.connect(exit,QtCore.SIGNAL('triggered()'),QtCore.SLOT('close()'))

        proj_menu.addAction(app)
        proj_menu.addAction(iploader)
        proj_menu.addAction(otaloader)
        proj_menu.addAction(exit)



























































































































































































































































































































































































































































































































































































































































































































































































       QQQQ)


























































































































































































































































































































































































































































































































































































































































































































































































       QQQQ


























































































































































































































































































































































































































































































































































































































































































































































































       QQQQ



















































































































































































































































































#! /usr/bin/env python
#coding:utf-8
#
# Copyright (C) 2008  Lorenzo Pallara, l.pallara@avalpa.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import os

from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.NIT import *
from dvbobjects.PSI.SDT import *
from dvbobjects.PSI.TDT import *
from dvbobjects.PSI.EIT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.DVB.Descriptors import *
from dvbobjects.MPEG.Descriptors import *

#
# Shared values
#

#Type Define
DVB_SERVICE_TYPE_TV = 1
OCN_OTA_DOWNLOADER_STREAM = 0xA1

transport_stream_id = 1 # demo value, an official value should be demanded to dvb org
original_transport_stream_id = 1 # demo value, an official value should be demanded to dvb org
LJ_network_id = 1
#
#
LJ_S01_service_id = 1 # demo value
LJ_S01_pmt_pid = 1031

LJ_DOWNLOAD_sid = 2 # demo value
LJ_DOWNLOAD_pmt_pid = 1302


#
# Network Information Table
# this is a basic NIT with the minimum desciptors, OpenCaster has a big library ready to use
#

nit = network_information_section(
	network_id = LJ_network_id,
        network_descriptor_loop = [
	    network_descriptor(network_name = "Longjing",),
	    linkage_descriptor(
			transport_stream_id = transport_stream_id,
			original_network_id = original_transport_stream_id,
			service_id = LJ_DOWNLOAD_sid,
			linkage_type = 0x91,
			manufacturer_id=0x15,
			hw_model=0x1200,
		  hw_version=0x1000,
		  sw_model=0x1200,
      sw_version=0x1016,
		  private_id=0x051600A0,
          download_mode_flag=0x00,
          download_group_count=0x03,
          serial_number_start1="\x00\x00\x00\x00\x00\x00\x00\x00",
          serial_number_end1="\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF",
          serial_number_start2="\x00\x00\x00\x00\x00\x00\x00\x00",
          serial_number_end2="\x00\x00\x00\x00\x00\x00\x00\x00",
          serial_number_start3="\x00\x00\x00\x00\x00\x00\x00\x00",
          serial_number_end3="\x00\x00\x00\x00\x00\x00\x00\x00",
      start_time_bytes = "\x11\x22\x33\x44\x55",
	    ),
            ],
	transport_stream_loop = [
	    transport_stream_loop_item(
		transport_stream_id = transport_stream_id,
		original_network_id = original_transport_stream_id,
		transport_descriptor_loop = [
		    service_list_descriptor(
			dvb_service_descriptor_loop = [
			    service_descriptor_loop_item(
				service_ID = LJ_S01_service_id,
				service_type = DVB_SERVICE_TYPE_TV, # digital tv service type
			    ),
			    service_descriptor_loop_item(
				service_ID = LJ_DOWNLOAD_sid,
				service_type = OCN_OTA_DOWNLOADER_STREAM, # digital tv service type
			    ),
			],
		    ),
		    transport_stream_cable_descriptor(
		    frequency =0x3790000 ,
		    FEC_outer =2,
		    modulation=3,
		    symbol_rate=0x69000,
		    FEC_inner=0xf,
		    ),
		],
	     ),

	  ],
        version_number = 10,# you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        )


#
# Program Association Table (ISO/IEC 13818-1 2.4.4.3)
#

pat = program_association_section(
	transport_stream_id = transport_stream_id,
        program_loop = [
    	    program_loop_item(
	        program_number = LJ_S01_service_id,
    		PID = LJ_S01_pmt_pid,
    	    ),
    	    #OTA Downloader service info
#    	    program_loop_item(
#	        program_number = LJ_DOWNLOAD_sid,
#    			PID = LJ_DOWNLOAD_pmt_pid,
#    	    ),
    	    program_loop_item(
	        program_number = 0, # special program for the NIT
    		PID = 16,
    	    ),
        ],
        version_number = 2, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        )


#
# Service Description Table (ETSI EN 300 468 5.2.3)
# this is a basic SDT with the minimum desciptors, OpenCaster has a big library ready to use
#

sdt = service_description_section(
	transport_stream_id = transport_stream_id,
	original_network_id = original_transport_stream_id,
        service_loop = [
	    service_loop_item(
		service_ID = LJ_S01_service_id,
		EIT_schedule_flag = 1, # 0 no current even information is broadcasted, 1 broadcasted
		EIT_present_following_flag = 1, # 0 no next event information is broadcasted, 1 is broadcasted
		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
		service_descriptor_loop = [
		    service_descriptor(
			service_type = DVB_SERVICE_TYPE_TV, # digital television service
			service_provider_name = "LJTV",
			service_name = "longjing",
		    ),
		],
	    ),
	    service_loop_item(
		service_ID = 2,
		EIT_schedule_flag = 1, # 0 no current even information is broadcasted, 1 broadcasted
		EIT_present_following_flag = 1, # 0 no next event information is broadcasted, 1 is broadcasted
		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
		service_descriptor_loop = [
		    service_descriptor(
			service_type = 0x80, # Is OTA download stream
			service_provider_name = "LJTV",
			service_name = "longjing",
		    ),
		],
	    ),
        ],
        version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        )



#
# Program Map Table (ISO/IEC 13818-1 2.4.4.8)
# this is a basic PMT the the minimum desciptors, OpenCaster has a big library ready to use
#

pmts1 = program_map_section(
	program_number = LJ_S01_service_id,
	PCR_PID = 800,
	program_info_descriptor_loop = [],
	stream_loop = [
		stream_loop_item(
			stream_type = 2, # mpeg2 video stream type
			elementary_PID = 800,
			element_info_descriptor_loop = []
		),
		stream_loop_item(
			stream_type = 4, # mpeg2 audio stream type
			elementary_PID = 860,
			element_info_descriptor_loop = [
			]
		),
	],
        version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        )


pmts2 = program_map_section(
	program_number = LJ_DOWNLOAD_sid,
	PCR_PID = 0x320,
	program_info_descriptor_loop = [],
	stream_loop = [
		stream_loop_item(
			stream_type = 2, # mpeg2 video stream type
			elementary_PID = 0x320,
			element_info_descriptor_loop = []
		),
		stream_loop_item(
			stream_type = 4, # mpeg2 audio stream type
			elementary_PID = 0x323,
			element_info_descriptor_loop = [
			]
		),
	],
        version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        )

#
# Time Description Table (ETSI EN 300 468 5.2.5)
# it should be replaced at run time with tstdt
#

tdt = time_date_section(
	year = 113, # since 1900
	month = 4,
	day = 26,
	hour = 0x03, # use hex like decimals
	minute = 0x53,
	second = 0x00,
        version_number = 1,
        section_number = 0,
        last_section_number = 0,
        )


#
# Event Information Table (ETSI EN 300 468 5.2.4)
#

#eit = event_information_section(
#	table_id = EIT_ACTUAL_TS_PRESENT_FOLLOWING,
#	service_id = avalpa1_service_id,
#	transport_stream_id = avalpa_transport_stream_id,
#	original_network_id = avalpa_original_transport_stream_id,
#        event_loop = [
#	    event_loop_item(
#		event_id = 1,
#		start_year = 108, # since 1900
#		start_month = 6,
#		start_day = 10,
#		start_hours = 0x00, # use hex like decimals
#		start_minutes = 0x00,
#		start_seconds = 0x00,
#		duration_hours = 0x23,
#		duration_minutes = 0x00,
#		duration_seconds = 0x00,
#		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
#		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
#		event_descriptor_loop = [
#		    short_event_descriptor (
#			ISO639_language_code = "ITA",
#			event_name = "epg event name",
#			text = "this is an epg event text example",
#		    ),
#		],
#	    ),
#            ],
#        segment_last_section_number = 1,
#        version_number = 1,
#        section_number = 0,
#        last_section_number = 1, # pay attention here, we have another section after this!
#        )
#
#
#eit_follow = event_information_section(
#	table_id = EIT_ACTUAL_TS_PRESENT_FOLLOWING,
#	service_id = avalpa1_service_id,
#	transport_stream_id = avalpa_transport_stream_id,
#	original_network_id = avalpa_original_transport_stream_id,
#        event_loop = [
#	    event_loop_item(
#		event_id = 2,
#		start_year = 108, # since 1900
#		start_month = 06,
#		start_day = 10,
#		start_hours = 0x23,
#		start_minutes = 0x30,
#		start_seconds = 0x00,
#		duration_hours = 0x12,
#		duration_minutes = 0x00,
#		duration_seconds = 0x00,
#		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
#		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
#		event_descriptor_loop = [
#		    short_event_descriptor (
#			ISO639_language_code = "ITA",
#			event_name = "epg event name 2",
#			text = "this is the following text example",
#		    )
#		],
#	    ),
#            ],
#        segment_last_section_number = 1,
#        version_number = 1,
#        section_number = 1, # this is the second section
#        last_section_number = 1,
#        )

#
# PSI marshalling and encapsulation
#
os.system('echo help')
out = open("./nit.sec", "wb+")
out.write(nit.pack())
out.close
out = open("./nit.sec", "wb") # python  flush bug
out.close
os.system('/usr/local/bin/sec2ts 16 < ./nit.sec > ./firstnit.ts')

out = open("./pat.sec", "wb")
out.write(pat.pack())
out.close
out = open("./pat.sec", "wb") # python   flush bug
out.close
os.system('/usr/local/bin/sec2ts 0 < ./pat.sec > ./firstpat.ts')

out = open("./sdt.sec", "wb")
out.write(sdt.pack())
out.close
out = open("./sdt.sec", "wb") # python   flush bug
out.close
os.system('/usr/local/bin/sec2ts 17 < ./sdt.sec > ./firstsdt.ts')

#out = open("./eit.sec", "wb")
#out.write(eit.pack())
#out.close
#out = open("./eit.sec", "wb") # python   flush bug
#out.close
#os.system('/usr/local/bin/sec2ts 18 < ./eit.sec > ./firsteit.ts')
#
#out = open("./eit_follow.sec", "wb")
#out.write(eit_follow.pack())
#out.close
#out = open("./eit_follow.sec", "wb") # python   flush bug
#out.close
#os.system('/usr/local/bin/sec2ts 18 < ./eit_follow.sec >> ./firsteit.ts')

out = open("./tdt.sec", "wb")
out.write(tdt.pack())
out.close
out = open("./tdt.sec", "wb") # python   flush bug
out.close
os.system('/usr/local/bin/sec2ts 20 < ./tdt.sec > ./firsttdt.ts')

out = open("./pmt.sec", "wb")
out.write(pmts1.pack())
out.close
out = open("./pmt.sec", "wb") # python   flush bug
out.close
os.system('/usr/local/bin/sec2ts ' + str(LJ_S01_pmt_pid) + ' < ./pmt.sec > ./firstpmt.ts')











































































































































































































































































































































































































       QQQQboard')
        self.connect(copy,QtCore.SIGNAL('triggered()'),self.slotOnClickCopy)

        paste = QtGui.QAction('Paste',self)
        paste.setShortcut('Ctrl+V')
        paste.setStatusTip('Paste')
        self.connect(paste,QtCore.SIGNAL('triggered()'),QtCore.SLOT('close()'))

        cut = QtGui.QAction('Cut',self)
        cut.setShortcut('Ctrl+X')
        cut.setStatusTip('Cut')
        self.connect(cut,QtCore.SIGNAL('triggered()'),QtCore.SLOT('close()'))

        edit_menu.addAction(copy)
        edit_menu.addAction(paste)
        edit_menu.addAction(cut)

        help_menu = menuBar.addMenu('&Help')
        about = QtGui.QAction('About',self)
        self.connect(about,QtCore.SIGNAL('triggered()'),self.slotOnClickAbout)
        help_menu.addAction(about)

    def slotOnClickApp(self):
        pass

    def slotOnClickIploader(self):
        pass

    def slotOnClickOtaloader(self):
        pass

    def slotOnClickCopy(self):
        self.text.copy()

    def slotOnClickAbout(self):
        QtGui.QMessageBox.aboutQt( self, "PyQt" )

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
