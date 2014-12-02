__author__ = 'djstava'

#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import socket

class DJTcpServer(object):
    def __init__(self):
        pass

    def dj_func_tcpServer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 8002))
        '''
        Max 5 connection
        '''
        sock.listen(5)

        while True:
            clientSock, (remoteHost, remotePort) = sock.accept()
            print("[%s:%s] connect" % (remoteHost, remotePort))

            revcData = clientSock.recv(1024)
            sendDataLen = clientSock.send("this is send  data from server")
            print "revcData: ", revcData
            print "sendDataLen: ", sendDataLen

            clientSock.close()

if __name__ == "__main__":
    dj_obj_tcpServer = DJTcpServer()
    dj_obj_tcpServer.dj_func_tcpServer()