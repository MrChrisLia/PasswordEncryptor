import cryptocode
import sqlite3
import requests
import base64
from tkinter import *
from tkinter import messagebox

# Passwords
# passwords = [("test", "itoc", "QF1"),
#              ("test", "itoc", " QF2")]

# To do: Create SQL DB to store
# connection = sqlite3.connect("passwords.db")
# cursor = connection.cursor()
#
# cursor.execute("create table passwords (password text, account text, website text)")
# cursor.executemany("insert into passwords values (?,?,?)", passwords)
#
# for row in cursor.execute("SELECT * FROM passwords"):
#     print(row)
#
# cursor.execute("SELECT * FROM passwords WHERE website=:w", {"w": "QF1"})
# account_search = cursor.fetchall()
# print(account_search)


# Main Window
root = Tk()
root.title('Password Vault 1.0')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
login_width = 500
login_height = 400
x = (screen_width / 2) - (login_width / 2)
y = (screen_height / 2) - (login_height / 2)
root.geometry(f'{login_width}x{login_height}+{int(x)}+{int(y)}')


def clear():
    my_text.delete(1.0, END)
    my_entry.delete(0, END)


def encrypt():
    secret = my_text.get(1.0, END)
    my_text.delete(1.0, END)
    if my_entry.get() == "ITOC":
        encrypted_txt = cryptocode.encrypt(secret, my_entry.get())
        my_text.insert(END, encrypted_txt)
    else:
        messagebox.showwarning("Error", "Incorrect Master Password! \n 主密碼不正確")


def decrypt():
    secret = my_text.get(1.0, END)
    my_text.delete(1.0, END)
    if my_entry.get() == "ITOC":
        decrypted_txt = cryptocode.decrypt(secret, my_entry.get())
        my_text.insert(END, decrypted_txt)
    else:
        messagebox.showwarning("Error", "Incorrect Master Password!\n 主密碼不正確")


my_frame = Frame(root)
my_frame.pack(pady=20)

enc_button = Button(my_frame, text="Encrypt 加密", command=encrypt)
enc_button.grid(row=0, column=0)

dec_button = Button(my_frame, text="Decrypt 解密", command=decrypt)
dec_button.grid(row=0, column=1)

clear_button = Button(my_frame, text="Clear 清除", command=clear)
clear_button.grid(row=0, column=2)

enc_label = Label(root, text='Enter Text Here \n 在此输入文字')
enc_label.pack()

my_text = Text(root, width=57, height=10)
my_text.pack(pady=10)

password_label = Label(root, text="Enter Master Password \n 輸入主密碼")
password_label.pack()

my_entry = Entry(root, width=35, show="*")
my_entry.pack(pady=10)


# connection.close()
root.mainloop()
