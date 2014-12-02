__author__ = 'djstava'

#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import socket

class DJUdpServer(object):
    def dj_func_udpServer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        '''
        server bind address which is a turple
        '''
        sock.bind(('', 8001))


        while True:
            revcData, (remoteHost, remotePort) = sock.recvfrom(1024)
            print("[%s:%s] connect" % (remoteHost, remotePort))

            sendDataLen = sock.sendto("this is send  data from server", (remoteHost, remotePort))
            print "revcData: ", revcData
            print "sendDataLen: ", sendDataLen

        sock.close()

if __name__ == "__main__":
    dj_obj_udpServer = DJUdpServer()
    dj_obj_udpServer.dj_func_udpServer()
