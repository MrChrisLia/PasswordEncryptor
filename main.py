from wsgiref import headers

import cryptocode
import sqlite3
import requests
import base64

# To do: Create SQL DB

# Basic Jira Authentication
auth_key = base64.b64encode(b"EMAIL:APIKEY").decode("ascii")
header = {"Authorization": "Basic " + auth_key}
response = requests.get("https://asiasupport247.atlassian.net/", headers=header)
print(response.status_code)


# To do: Create a login GUI. If status code is 200, it means you can authenticate to Atlassian,
# thus unlocking the passwords. If status code isn't 200, it means you can't authenticate to Atlassian,
# thus cannot unlock the passwords



def encryptor(password, username):
  str_encoded = cryptocode.encrypt(password, username)
  print('Success!')
  print(str_encoded)


encryptor('test', 'itoc')


def decryptor(password, username):
  str_decoded = cryptocode.decrypt(password, username)
  print('Success!')
  print(str_decoded)


decryptor('sjoQiw==*6ZimfHrY9HUxCySi2hzkKA==*vDCkTKVgOK0ukyQyXYq3hg==*1BuhkAfKx7Qf2AmQDeUj4A==', 'itoc')
