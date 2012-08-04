#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import json
import time
import random
import os

import sys
import pynotify

from lib import fbconsole
from optparse import OptionParser

tmp = os.path.dirname( os.path.abspath(__file__) ) + '/tmp/'

guide = "usage: %prog [options]"
parser = OptionParser(usage=guide)

parser.add_option('-v','--verbose',action='store_false',help='verbose mode',dest='verbose')
parser.add_option('-m','--mark',action='store_false',help='auto mark notifications as read',dest='mark')

(options,args) = parser.parse_args()

#pynotify.Notification method
def notify(title,msg,photo):
	n = pynotify.Notification (title,msg,photo) #"notification-message-im"
	n.show ()

class notf:
    def __init__(self):
        pass
    def notfy(self):
        try:
            #fbconsole method
            fbconsole.AUTH_SCOPE = ['manage_notifications']
            fbconsole.authenticate()

            time.sleep(random.randint(30,120))
        
            #facebook ID
            ID = 'len.tw'
        
            #Graph API access_token

            #print fbconsole.ACCESS_TOKEN
            token = fbconsole.ACCESS_TOKEN

            req = urllib2.Request( 'https://graph.facebook.com/'+ ID + '/notifications?access_token=' + token )
            req.add_header( 'User-agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6' )
            try: r = urllib2.urlopen( req )
            except urllib2.URLError:
               pass 

            jr = json.load( r ) 

            for data in jr["data"]:
                if data == '' :
                    continue
                name = data["from"]["name"]  # notify from who
                msg  = data["title"]         # notify summary
                photoID = data["from"]["id"] # Got notify from who's ID

                # Cache avatar
                photo = 'https://graph.facebook.com/' + photoID + '/picture'
                tmpPhoto = tmp + photoID
                urllib.urlretrieve(photo,tmpPhoto)

                notify(name,msg,tmpPhoto)

        # HOLD Ctrl+c event
        except KeyboardInterrupt:
            fbconsole.logout()
            print '\nLog out'
            exit(0)

if __name__ == '__main__':
    if not pynotify.init ("icon-summary-body"):
        sys.exit (1)

    if os.path.exists( tmp ):
        pass
    else:
        print 'mkdir tmp/ ...' ,
        try:
            os.makedirs( tmp )
        except OSError:
            print 'cannot mkdir tmp'
            sys.ext(1)
        print 'success'
    while(1):
        notf().notfy()
