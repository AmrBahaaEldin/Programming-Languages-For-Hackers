#!/usr/bin/python3
import requests
url="http://testphp.vulnweb.com/login.php"
response=requests.get(url)
                  
print(response.status_code)

#payload:Data post=>web 
#search input name 
payload="uname=test&pass=test"
response=requests.post(url,data=payload)
print(response.status_code)