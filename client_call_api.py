import sys
import requests
import json

mac_address = input("Please enter mac address:")
max_len = len(mac_address)

if (max_len < 8): 
	print ('Please enter atleast 8 characters with xx-xx-xx format')
	sys.exit(0)

mac_address = mac_address[0:8]
url = 'http://localhost:81/test/mac_address_lookup_api.py'

payload = {
    'mac_address': mac_address,
	'token': '123456'
}

#response = requests.post(url, data=payload,headers={"Content-Type": "application/json"})
response = requests.post(url, data=payload)

if response.status_code == 200:
	print(response.text)
else:
	print('Invalid response...')

#print(response.json())
#print(json.loads(response.text)['session'])