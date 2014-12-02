__author__ = 'djstava'

#!/usr/bin/env python
#coding=utf-8

import getopt
import sys

def dj_commandLine_parse():
    for str in sys.argv:
        print str

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        dj_commandLine_usage()
        sys.exit()

    output = None
    verbose = False

    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            dj_commandLine_usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"

def dj_commandLine_usage():
    print 'dj_commandLine.py usage:'
    print '-h,--help: print help message.'
    print '-v, --version: print script version'
    print '-o, --output: input an output verb'

if __name__ == "__main__":
    dj_commandLine_parse()