import cgi
from webaroo import mSend
from google.appengine.ext import ndb

class Emails(ndb.Model):
	phone = ndb.StringProperty()
	content = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)

class Logs(ndb.Model):
	response = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)			

form = cgi.FieldStorage()
print "Content-type:text/html\r\n\r\n"

rec = form.getvalue('recipient')
sender = form.getvalue('From')
subject = form.getvalue('subject')
data = form.getvalue('stripped-text')
num = rec.split("@")

#Storage logic
email = Emails(parent=ndb.Key('Emails', '*notitle'), phone=num[0], content=subject)
email.put()

#Send SMS
newSMS = mSend(num[0], subject)
result = newSMS.send()

#Log response
log = Logs(parent=ndb.Key('Log', '*notitle'), response=result)
log.put()

#newSMS = Way2sms('http://site24.way2sms.com', '9665215267', 'asdfgh')
#newSMS.login()
#newSMS.getToken()
#newSMS.sendSMS(num[0], subject+','+sender)

