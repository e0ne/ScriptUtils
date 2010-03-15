#!/usr/bin/env python

import urllib2
import re
import os
import sys
import getopt

def main():
    svnUrl = ''
    srcPath = ''
    username = ''
    password = ''
    checkOut = True
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'supfhm:v', ['server=',
                                                         'user=',
                                                         'password=',
                                                         'folder=',
                                                         'help',
                                                         'mode='
                                                         ])
        for o, a in opts:
           if o in ("--server", "-s"):
               svnUrl = a
           elif o in ("--user", "-u"):
               username = a
           elif o in ("--password", "-p"):
               password = a
           elif o in ("--folder", "-f"):
               srcPath = a
           elif o in ("--help", "h"):
               help()
           elif o in ("--mode", "m"):
               if a == 'update':
                   checkOut = False

    except getopt.GetoptError, err:
       # print help information and exit:
       print str(err) # will print something like "option -a not recognized"
       sys.exit(2)


    response = urllib2.urlopen(svnUrl)
    svnPage = response.read()

    links = re.finditer('href="?([^\s^"]+)/', svnPage)

    for link in links:
        # NOTE: temporary fix
        if link =='http:subversion.tigris.org':
            continue
        # TODO: update regexp
        name = link.group(0).replace('href="', '').replace('/', '')
        print 'Student: ', name
        print 'Getting sourses...'
        path = srcPath + name
        if checkOut:
            os.system('mkdir ' + path)
            command = "checkout"
        else:
             command = "update"
        os.system('svn ' + command + ' ' + svnUrl + '/' + name + ' ' + path +' --username ' + username + ' --password ' + password)

def help():
    print "Arguments help will be here."
    print "Requirements:"
    print "Windows: http://docs.codehaus.org/display/GEOT/SVN+Windows"

if __name__ == "__main__":
    main()