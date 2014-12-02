__author__ = 'djstava'

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import re
import string
import telnetlib
import sqlite3
import codecs
from time import ctime,sleep
import threading
import socket
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

TIMEOUT = 3
conf.verb = 0
itemCount = 0

def dj_scanIPAddr(suffix):

    dst = "192.168.1." + str(suffix)
    packet = IP(dst = dst, ttl = 20) / ICMP()
    reply = sr1(packet, timeout = TIMEOUT)
    if not (reply is None):
        #print reply.src + " is online "
        return 1
    else:
        return 0


def dj_getRandomNubFromSqlite3(serialNum):

    randomNum = ""
    conn = sqlite3.connect('tscdata.db')
    cursor = conn.cursor()

    queryCommand = "select SN,PRIVATEDATA from tscdata where SN=" + '"' + serialNum + '"'
    #print queryCommand
    #print "sqlite3 serial num  = " + serialNum
    cursor.execute(queryCommand)
    res = cursor.fetchall()
    #print res
    for line in res:
        for h in line:
            if h == serialNum:
                continue;
            else:
                randomNum = h[8:16]
                #print randomNum

    conn.close()
    return randomNum

def main():

    threads = []
    commands = ["mount -o nolock 192.168.1.250:/tftpboot /mnt","cd /mnt","./testsysinfo -g STB_BBCB_SN_RANDNUMBER","./testsysinfo -s STB_IRDETO_KEY '1'","exit"]

    fd = open('rescue.log','wb')

    for i in range(100,201):
        ret = dj_scanIPAddr(i)
        print "ip is " + str(i) + ",Ret is: " + str(ret)
        if ret == 1:
            dstIP = "192.168.1." + str(i)
            print dstIP + " is online."
            th = threading.Thread(target = dj_telnet_connect,args = (dstIP,"root","",commands,fd))
            threads.append(th)
        else:
            continue

    for th in threads :
        th.start()

    for th in threads :
        th.join()

    fd.close()
    print "\nExit main function|"

def dj_telnet_connect(Host, username, password,commands,handler):

    enter = '\n'
    serialNum = ""
    serialNum_ori = ""
    randomNum = ""
    randomNum_orig = ""

    t = telnetlib.Telnet(Host)

    t.read_until("login: ",1)
    t.write(username + enter)

    t.read_until("Password: ",1)
    t.write(password + enter)

    #print "Congratulations,telnet is OK,start to rescue."

    for command in commands:

        if command.find("testsysinfo -g STB_BBCB_SN_RANDNUMBER") != -1:
            #print "Meet get SN statement" + enter
            t.write('%s\n' % command)
            sleep(2)
            res = t.read_very_eager()
            #print "djstava:" + res
            ret = res.find("vlaue is")
            if ret != -1:
                serialNum = res[ret + 9:ret + 20]
                randomNum_orig = (res[ret + 21:ret + 32]).replace('-','')
                print "Serial Number is : " + serialNum
                print "OOOOOOOOOOOOOOOOOOOrig random number is:" + randomNum_orig + ",MAC is: " + dj_getMacAddr(Host) + ",IP is: " + Host

                if string.atol(randomNum_orig,16) != 0:
                    #print "No need to rescue."
                    handler.write(Host + "  MAC: " + dj_getMacAddr(Host) + " ,No need to rescue." + enter)
                    break
                else:
                    serialNum_ori = serialNum.replace('-','')

                    randomNum = dj_getRandomNubFromSqlite3(serialNum_ori.upper())
                    print "Random Number in DB is : " + randomNum
                    setRNCommand = "./testsysinfo -s STB_BBCB_SN_RANDNUMBER" + ' "' +serialNum + '-' + randomNum[0:2] + '-' + randomNum[2:4] + '-' + randomNum[4:6] + '-' +randomNum[6:8] + '"' + enter

                    #print setRNCommand
                    t.write(setRNCommand.encode("ascii"))
                    handler.write(Host + "  MAC: " + dj_getMacAddr(Host) + " ,has been rescued." + enter)

            else:
                print "Get SN wrong."
        else:
            t.write('%s\n' % command)

    global itemCount
    itemCount += 1

    if itemCount % 5 == 0:
        handler.write(enter)

    t.close()

def dj_getMacAddr(ip):

    pattern_mac = re.compile('([a-f0-9]{2}[-:]){5}[a-f0-9]{2}', re.I)
    os.popen('ping -nq -c 1 -W 500 {} > /dev/null'.format(ip))
    result = os.popen('arp -an {}'.format(ip))
    result = pattern_mac.search(result.read())
    return result.group() if result else None

def dj_getMacAddr_local():

    mac = ""
    for line in os.popen("/sbin/ifconfig"):
        print line
        if 'HWaddr' in line:
            mac = line.split()[4]
            break

    return mac

if __name__ == '__main__':
    main()
