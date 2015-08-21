import cgi
from smslib import Way2sms
from google.appengine.ext import ndb

class Emails(ndb.Model):
	phone = ndb.StringProperty()
	content = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)

form = cgi.FieldStorage()
print "Content-type:text/html\r\n\r\n"

rec = form.getvalue('recipient')
sender = form.getvalue('From')
subject = form.getvalue('subject')
data = form.getvalue('stripped-text')
credentials = rec.split("@")[0].split("_")

way2_username = credentials[0]
way2_password = credentials[1]

#Storage logic
email = Emails(parent=ndb.Key('Emails', '*notitle'), phone=way2_username, content=subject)
email.put()

#Send SMS
newSMS = Way2sms('http://site24.way2sms.com', way2_username, way2_password)
newSMS.login()
newSMS.getToken()
newSMS.sendSMS(way2_username, subject+','+sender)