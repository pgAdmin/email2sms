import cgi
from smslib import Way2sms
from google.appengine.ext import ndb

way2_username = '9999999999'
way2_password = 'password'

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
num = rec.split("@")

#Storage logic
email = Emails(parent=ndb.Key('Emails', '*notitle'), phone=num[0], content=subject)
email.put()

#Send SMS
newSMS = Way2sms('http://site24.way2sms.com', way2_username, way2_password)
newSMS.login()
newSMS.getToken()
newSMS.sendSMS(num[0], subject+','+sender)

#request_body = "uid=9665215267&pwd=asdfgh&phone="+num[0]+"&msg="+subject+","+sender
#url = "http://spirit1552.pagebit.net/way2sms/wy.php"
#result = urlfetch.fetch(url, payload=request_body, method=urlfetch.POST, deadline=5)
#print result