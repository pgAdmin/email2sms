import urllib2

class mSend:
    def __init__(self, mobile, message):
        message = message[0:140]
        header_data={"X-Mashape-Key": "sVJlEu5hhmmsh9EHmCQ2QSsFL6xip1uaEbDjsn7wUARecriMKS"}
        self.req = urllib2.Request("https://webaroo-send-message-v1.p.mashape.com/sendMessage?message="+message+"&phone="+mobile, headers=header_data)
    
    def send(self):    
        response = urllib2.urlopen(self.req).read()
        return response