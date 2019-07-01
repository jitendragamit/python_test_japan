#!/usr/bin/env python
#print('Content-Type: text/html')
print('\r') 
#print('Hello, world!')
import request
import mysql.connector
import json

data = request.POST
python_obj = json.dumps(data)
python_obj = json.loads(python_obj)
mac_address = python_obj['mac_address']
token = python_obj['token']

if token != '123456':
	print('Invalid token value')
	sys.exit(0)

	
conn = mysql.connector.connect(host='localhost',
                             database='db_python_test',
                             user='root',
                             password='')
							 
cursor = conn.cursor()

query = "SELECT vendor_name FROM tbl_mac_address_vendor where address_prefix like '" + mac_address + "%'"

cursor.execute(query)
rows = cursor.fetchone()

if cursor.rowcount > 0:
	vendor_name = rows[0]
	print(vendor_name)
else :
	print("Not found company for this mac address") 
	
cursor.close()






