__author__ = 'djstava'

#!/usr/bin/env python
#coding=utf-8

import pycurl
import sys

DJ_PYCURL_CONNECTTIMEOUT = 30
DJ_PYCURL_TIMEOUT = 300
DJ_PYCURL_DOWNLOADURL = "http://192.168.1.182/test.zip"
DJ_PYCURL_DOWNLOAD_FILE = "download.file"

fp = open(DJ_PYCURL_DOWNLOAD_FILE,'wb+')

def dj_pycurl_writeFile(buffer):
    fp.write(buffer)

def dj_pycurl_download(url):
    pycurl.global_init(pycurl.GLOBAL_ALL)
    c = pycurl.Curl()

    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.WRITEDATA,fp)
    c.setopt(pycurl.WRITEFUNCTION,dj_pycurl_writeFile)
    c.setopt(pycurl.NOPROGRESS,0)
    c.setopt(pycurl.CONNECTTIMEOUT,DJ_PYCURL_CONNECTTIMEOUT)
    c.setopt(pycurl.TIMEOUT,DJ_PYCURL_TIMEOUT)
    c.setopt(pycurl.VERBOSE,1)

    c.perform()
    c.close()
    fp.close()

if __name__ == '__main__':
    dj_pycurl_download(DJ_PYCURL_DOWNLOADURL)
