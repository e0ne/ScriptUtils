#!/usr/bin/env python

import re
import os
import sys
import getopt

def main():
    mode = ''
    envName = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'supfhm:v', ['mode=',
                                                         'envName=',
                                                         'help'
                                                         ])
        for o, a in opts:
           if o in ("--mode", "-s"):
               mode = a
           elif o in ("--envName", "-u"):
               envName = a

    except getopt.GetoptError, err:
       # print help information and exit:
       print str(err) # will print something like "option -a not recognized"
       sys.exit(2)

def help():
    print "Help:"

if __name__ == "__main__":
    main()