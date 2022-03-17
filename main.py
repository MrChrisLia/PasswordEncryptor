from wsgiref import headers

import cryptocode
import sqlite3
import requests
import base64

# Passwords
passwords = [("test", "itoc", "QF1"),
             ("test", "itoc", " QF2")]

# To do: Create SQL DB to store
connection = sqlite3.connect("passwords.db")
cursor = connection.cursor()

cursor.execute("create table passwords (password text, account text, website text)")
cursor.executemany("insert into passwords values (?,?,?)", passwords)

for row in cursor.execute("SELECT * FROM passwords"):
    print(row)

cursor.execute("SELECT * FROM passwords WHERE website=:w", {"w": "QF1"})
account_search = cursor.fetchall()
print(account_search)
# Basic Jira Authentication

# auth_key = base64.b64encode(b"christopher.lia@luanta.com.tw:Tatsz4c9KZdjiFvaf4Bc4B09").decode("ascii")
# header = {"Authorization": "Basic " + auth_key}
# response = requests.get("https://asiasupport247.atlassian.net/", headers=header)
# print(response.status_code)


# To do: Create a login GUI. If status code is 200, it means you can authenticate to Atlassian,
# thus unlocking the passwords. If status code isn't 200, it means you can't authenticate to Atlassian,
# thus cannot unlock the passwords



# def encryptor(password, username, platform):
#   str_encoded = cryptocode.encrypt(password, username)
#   print('Successfully encrypted! Please paste this to our Confluence Page. ' + str_encoded)
#
#
# encryptor('test', 'itoc')
#
#
# def decryptor(password, username, platform):
#   str_decoded = cryptocode.decrypt(password, username)
#   print('Successfully decrypted! ' + str_decoded)


connection.close()