import requests, json

config = json.load(open('config.json'))
username = config['username']
password = config['password']

r = requests.get('https://event-svc-pvt.sxsw.com/goodattheinternet/', auth=(username, password))

data = json.loads(r.text)

print 'DATA', data