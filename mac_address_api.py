#!C:/Users/jgamit/AppData/Local/Programs/Python/Python36/python.exe
#print('Content-Type: text/html')
print('\r') 
import request
import mysql.connector
import json

data = request.POST

python_obj = json.dumps(data)

python_obj = json.loads(python_obj)

max_address = python_obj['max_address']

conn = mysql.connector.connect(host='localhost',
                             database='db_python_test',
                             user='root',
                             password='')
							 
cursor = conn.cursor()
query = "SELECT vendor_name FROM tbl_mac_address_vendor where address_prefix like '" + max_address + "%'"

cursor.execute(query)
rows = cursor.fetchone()
print(rows[0])
cursor.close()






