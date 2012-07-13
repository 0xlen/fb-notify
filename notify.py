#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
# fb-notify

Copyright (C) 2012 Len @ http://len.hack-stuff.com
# All rights reversed.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom
the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
'''

import urllib2
import urllib
import json
import time
import random
import os

import sys
import pynotify

from lib import fbconsole

#fbconsole method
fbconsole.AUTH_SCOPE = ['manage_notifications']
fbconsole.authenticate()


tmp = os.path.dirname(os.path.abspath(__file__)) + '/tmp/'


if __name__ == '__main__':
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

    if not pynotify.init ("icon-summary-body"):
        sys.exit (1)


#pynotify.Notification method
def notify(title,msg,photo):
	n = pynotify.Notification (title,msg,photo) #"notification-message-im"
	n.show ()

#notify loop
while(1):
    time.sleep(random.randint(30,120))
    
    #facebook ID
    ID = 'len.tw'
    
    #Graph API access_token

    #print fbconsole.ACCESS_TOKEN
    token = fbconsole.ACCESS_TOKEN

    req = urllib2.Request('https://graph.facebook.com/'+ ID + '/notifications?access_token='+token)
    req.add_header('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6')
    r = urllib2.urlopen(req)

    jr = json.load( r ) 

    for data in jr["data"]:
        name = data["from"]["name"]  #notify from who
        msg  = data["title"]         #notify summary
        photoID = data["from"]["id"] #Got notify from who's ID
        photo = 'https://graph.facebook.com/' + photoID + '/picture'
        tmp += photoID
        urllib.urlretrieve(photo,tmp)
        notify(name,msg,tmp)
