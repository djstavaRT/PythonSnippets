__author__ = 'djstava'

#!/usr/bin/env python
# -*- coding:utf8 -*-

import sys
import socket

class DJUdpClient(object):
    def dj_func_tcpclient(self):
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sendDataLen = clientSock.sendto("This is send data from client", ('localhost', 8001))
        recvData = clientSock.recvfrom(1024)
        print "sendDataLen: ", sendDataLen
        print "recvData: ", recvData

        clientSock.close()

if __name__ == "__main__":
    dj_obj_udpClient = DJUdpClient()
    dj_obj_udpClient.dj_func_tcpclient()