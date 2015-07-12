import cookielib
import urllib
import urllib2

class Way2sms:
    def __init__(self, uri, username, password):
        self.uri = uri
        self.username = username
        self.password = password        
        self.cookies = cookielib.LWPCookieJar()
        self.handlers = [
            urllib2.HTTPHandler(),
            urllib2.HTTPSHandler(),
            urllib2.HTTPCookieProcessor(self.cookies)
        ]

    def login(self):
        data = 'username='+self.username+'&password='+self.password
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.2) Gecko/20100101 Firefox/24.0'}
        req = urllib2.Request(self.uri+'/Login1.action', data, headers)
        opener = urllib2.build_opener(*self.handlers)
        return opener.open(req)

    def sendSMS(self, mobile, message):
        headers = {'Referer': self.uri+'/sendSMS.action?Token='+self.token, 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.2) Gecko/20100101 Firefox/24.0'}
        message = message[0:140]
        data = 'ssaction=ss&Token='+self.token+'&mobile='+mobile+'&message='+message+'&msgLen='+str(140-len(message))
        req = urllib2.Request(self.uri+"/smstoss.action", data, headers)
        opener = urllib2.build_opener(*self.handlers)
        return opener.open(req)

    def getToken(self):
        for cookie in self.cookies:
            if cookie.name == 'JSESSIONID':
                self.token = cookie.value[4:]

