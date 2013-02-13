import json, urllib2, base64

config = json.load(open('config.json'))
print 'CONFIG', config
username = config['username']
password = config['password']

request = urllib2.Request("https://event-svc-pvt.sxsw.com/goodattheinternet")
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
response = urllib2.urlopen(request)

data = json.load(response)

print 'DATA', data