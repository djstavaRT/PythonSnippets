__author__ = 'djstava'

#!/usr/bin/env python
# -*- coding: utf-8 -*

import wx
import telnetlib

DJ_AUTOTESTFORIPLOADER_LOG = "log.txt"

class DJMainFrame(wx.Frame):
    def __init__(self,parent,id,title,pos,size):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        self.panel = wx.Panel(self)
        self.icon = wx.Icon('djstava.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self.panel.SetBackgroundColour('white')

        '''
        self.statusBar = self.CreateStatusBar()
        self.toolBar = self.CreateToolBar()
        self.toolBar.AddSimpleTool(wx.NewId(),wx.Bitmap('djstava.bmp'),"New","long help for 'New'")
        self.toolBar.Realize()
        '''

        menuBar = wx.MenuBar()

        projectMenu = wx.Menu()
        appItem = projectMenu.Append(wx.NewId(),"&App","")
        projectMenu.AppendSeparator()

        iploaderItem = projectMenu.Append(wx.NewId(),"&Iploader","Upgrade from IP")
        projectMenu.AppendSeparator()

        otaloader = projectMenu.Append(wx.NewId(),"&Otaloader","Upgrade from HFC")
        projectMenu.AppendSeparator()

        exitItem = projectMenu.Append(wx.NewId(),"&Exit","")
        menuBar.Append(projectMenu,"&Projects")

        self.Bind(wx.EVT_MENU,self.onProjectApp,appItem)
        self.Bind(wx.EVT_MENU,self.onProjectIploader,iploaderItem)
        self.Bind(wx.EVT_MENU,self.onProjectOtaloader,otaloader)
        self.Bind(wx.EVT_MENU,self.onProjectExit,exitItem)

        editMenu = wx.Menu()
        editMenu.Append(wx.NewId(),"&Copy","Copy in status bar")
        editMenu.Append(wx.NewId(),"&Cut","")
        editMenu.Append(wx.NewId(),"&Paste","")
        editMenu.AppendSeparator()
        editMenu.Append(wx.NewId(),"&Options...","Display Options")
        menuBar.Append(editMenu,"&Edit")

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.NewId(),"About","")
        menuBar.Append(helpMenu,"&Help")

        self.Bind(wx.EVT_MENU,self.onHelpAbout,aboutItem)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        self.SetMenuBar(menuBar)
        '''
        self.dj_button_connect = wx.Button(self.panel,label = "connect",pos = (260,40),size = (80,40))
        self.dj_button_clear = wx.Button(self.panel,label = "clear",pos = (360,40),size = (80,40))
        self.dj_lineedit_telnetUrl = wx.TextCtrl(self.panel,value = "192.168.1.128",pos = (20,40),size = (120,40))

        self.Bind(wx.EVT_BUTTON,self.OnClick_buttion_connect,self.dj_button_connect)
        self.Bind(wx.EVT_BUTTON,self.OnClick_buttion_clear,self.dj_button_clear)
        '''

    def OnCloseWindow(self, event):
        self.Destroy()

    def onProjectApp(self,event):
        pass

    def onProjectIploader(self,event):
        pass

    def onProjectOtaloader(self,event):
        pass

    def onProjectExit(self,event):
        self.Close()

    def onHelpAbout(self,event):
        description = '''This program is aim to test embedded devices like Set Top Box automatically.Powered by wxPython.'''

        licence = '''The MIT License (MIT)

Copyright (c) 2014 djstava

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

        info = wx.AboutDialogInfo()
        info.SetIcon(wx.Icon('djstava.ico',wx.BITMAP_TYPE_ICO))
        #set program name
        info.SetName('AutoTestKit')
        info.SetVersion('1.0.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2014 djstava')
        info.SetWebSite('http://macernow.com')
        info.SetLicence(licence)
        info.AddDeveloper('djstava')
        info.AddDocWriter('djstava')
        info.AddArtist('djstava')
        info.AddTranslator('djstava')

        wx.AboutBox(info)

    def ipAddressIsValidate(self,ipAddr):
        addr = ipAddr.strip().split('.')

        if len(addr) != 4:
            print("ipAddr is invalidate.")
            return False

        if ipAddr == '0.0.0.0':
            return False

        for i in range(4):
            try:
                addr[i] = int(addr[i])
            except:
                print("ipAddr is invalidate.")
                return False
            if addr[i] <= 255 and addr[i] >= 0:
                pass
            else:
                print("ipAddr is invalidate.")
                return False

            i += 1

        print("ipAddr is validate.")
        return True

    def OnClick_buttion_connect(self,event):
        if self.dj_lineedit_telnetUrl.IsEmpty():
            print("telnetUrl is empty.")
        else:
            dj_telnetUrl = self.dj_lineedit_telnetUrl.GetValue()
            if self.ipAddressIsValidate(dj_telnetUrl):
                self.dj_telnet_connect(dj_telnetUrl,"root","","ifconfig")
            else:
                dlg = wx.MessageDialog(self,"IPAddress error! Please try another.","Error",style = wx.OK | wx.ICON_ERROR)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Destroy()

    def OnClick_buttion_clear(self,event):
        self.dj_lineedit_telnetUrl.SetValue("")

    def dj_telnet_connect(self,host, username, password, command):
        enter = '\n'
        t = telnetlib.Telnet(host)
        t.set_debuglevel(2)
        t.open(host,23,3)
        t.read_until("login: ",1)
        t.write(username + enter)
        t.read_until("Password: ",1)
        t.write(password + enter)
        t.write(command + enter)
        t.read_until("#")
        t.close()

if __name__=='__main__':
    dj_mainApp = wx.PySimpleApp()
    frame = DJMainFrame(parent = None,id = wx.NewId(),title = "AutoTestKit",pos = (0,0),size = (460,400))
    frame.Show()
    dj_mainApp.SetTopWindow(frame)
    dj_mainApp.MainLoop()