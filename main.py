import cryptocode

def encryptor(password,username):
  str_encoded = cryptocode.encrypt(password, username)
  print('Success!')
  print(str_encoded)


encryptor('test', 'itoc')


def decryptor(password, username):
  str_decoded = cryptocode.decrypt(password, username)
  print('Success!')
  print(str_decoded)

decryptor('sjoQiw==*6ZimfHrY9HUxCySi2hzkKA==*vDCkTKVgOK0ukyQyXYq3hg==*1BuhkAfKx7Qf2AmQDeUj4A==', 'itoc')
