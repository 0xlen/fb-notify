from lib import fbconsole
import urllib2

fbconsole.AUTH_SCOPE = ['manage_notifications']
fbconsole.authenticate()

print fbconsole.ACCESS_TOKEN

req = urllib2.Request('http://www.facebook.com/Len.tw/posts/464243160261666?ref=notif')

req.add_header('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6')

r = urllib2.urlopen(req)

print r.read()

fbconsole.logout()
