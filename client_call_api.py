#from pexpect import pxssh
import sys
import requests
import json

#s = pxssh.pxssh()
mac_address = input("Please enter mac address:")

#s.prompt()
#s.setecho(True)

max_len = len(mac_address)

#mac_address = sys.argv[1]
#max_len = len(mac_address)

if (max_len < 8): 
	print ('Please enter atleast 8 characters with xx-xx-xx format')
	sys.exit(0)

mac_address = mac_address[0:8]
url = 'http://localhost:81/test/mac_address_lookup_api.py?mac_address=' + mac_address + '&token=123456'

#response = requests.post(url, data=payload,headers={"Content-Type": "application/json"})
response = requests.get(url)

if response.status_code == 200:
	print(response.text)
else:
	print('Invalid response..')
