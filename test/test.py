from lib import fbconsole


fbconsole.AUTH_SCOPE = ['manage_notifications']
fbconsole.authenticate()

print fbconsole.ACCESS_TOKEN
