__author__ = 'djstava'

#!/usr/bin/env python
#coding=utf-8

import telnetlib

def dj_telnet_connect(Host, username, password, command):

    enter = '\n'

    t = telnetlib.Telnet(Host)

    t.read_until("login: ",1)
    t.write(username + enter)

    t.read_until("Password: ",1)
    t.write(password + enter)

    t.write(command + enter)
    #print t.read_all()

    print "Congratulations."

    t.write("exit" + enter)
    print t.read_all()
    t.close()

if __name__ == '__main__':
    host = '192.168.1.32'
    username = 'root'
    password = ''
    #command = 'mount -o nolock 192.168.1.250:/tftpboot/ /mnt & /mnt/testsysinfo -g STB_BBCB_SN_RANDNUMBER'
    command = "ifconfig"
    dj_telnet_connect(host, username, password, command)