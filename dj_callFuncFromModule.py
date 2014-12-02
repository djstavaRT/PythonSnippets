__author__ = 'djstava'

#!/usr/bin/env python
#coding=utf-8

import sys
from dj_telnet import *

if __name__=='__main__':

	Host = '192.168.1.109'
	username = 'root'
	password = ''
	command = 'pwd'
	dj_telnet_connect(Host, username, password, command)