import sys
import requests

mac_address = input("Please enter mac address:")
url = 'http://localhost:81/python_dev/mac_address_api.py'

payload = {
    'max_address': mac_address
}

response = requests.post(url, data=payload)

print(response.text)

