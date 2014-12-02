__author__ = 'djstava'

#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import socket

class DJTcpClient(object):
    def __init__(self):
        pass

    def dj_func_tcpclient(self):
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSock.connect(('localhost', 8002))

        sendDataLen = clientSock.send("this is send data from client")
        recvData = clientSock.recv(1024)
        print "sendDataLen: ", sendDataLen
        print "recvData: ", recvData

        clientSock.close()

if __name__ == "__main__":
    dj_obj_tcpClient = DJTcpClient()
    dj_obj_tcpClient.dj_func_tcpclient()