"""
@date: 2023/8/31
@author: March
@desc: test

"""
import requests
import json

url = "http://192.168.1.115:5000/login2"

payload = json.dumps({
  "username": "root",
  "passwd": 123456
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
