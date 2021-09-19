from tkinter import *
from urllib.request import urlopen
import ast

#auto-py-to-exe
#AurorA Fishbot 1.6v

#pyarmor obfuscate foo.py
#cd dist
#pyinstaller --noconfirm --onefile --windowed --icon "C:/Users/Dawid/PycharmProjects/Aurora/icon.ico" --add-data "C:/Users/Dawid/PycharmProjects/Aurora/images;." --upx-dir=C:\Users\Dawid\PycharmProjects\Aurora\upx-3.96-win64 "C:/Users/Dawid/PycharmProjects/Aurora_raw/Aurora_main.py"

# Designing window for login



def sql_parsing():
    global usernames, passwords, expired

    usernames = []
    passwords = []
    expired = []

    #https://pastebin.com/ZRBPy5ng

    sql_login = urlopen('https://pastebin.com/raw/ZRBPy5ng')
    sql_login = sql_login.read().strip()
    sql_login = sql_login.decode('utf-8')
    sql_login = sql_login.splitlines()

    for i in range(len(sql_login)):
        sql_login[i] = sql_login[i].split("*")

    for i in range(len(sql_login)):
        usernames.append(sql_login[i][0])
        passwords.append(sql_login[i][1])
        expired.append(ast.literal_eval(sql_login[i][2]))



def server_time():
  time = urlopen('http://just-the-time.appspot.com/')
  time = time.read().strip()
  time = time.decode('utf-8')
  time_split = time.split(" ")
  time_split = time_split[0].split("-")
  for i in range(0, len(time_split)):
    time_split[i] = int(time_split[i])
  return(time_split)

def function_server_time_flag(user):
    time = server_time()
    for i in range(3):
        if expired[user][i] > time[i]:
            return(1)
        elif expired[user][i] < time[i]:
            return(0)

def login():
    global login_screen,login_status
    login_status = 0
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="AurorA Albion Fishbot 1.6v").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    global password_entry,username_entry

    Label(login_screen, text="LOGIN").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="PASSWORD").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

    login_screen.mainloop()

    return(username_entry,password_entry,login_status)

# Implementing event on login button



def login_verify():
    global login_screen, usernames, passwords, expired,username_entry,password_entry,login_status

    username_entry = username_verify.get()
    password_entry = password_verify.get()

    sql_parsing()

    for user in range(len(usernames)):
        if username_entry == usernames[user]:
            if password_entry == passwords[user]:
                if function_server_time_flag(user) == 1:    #success
                    login_screen.destroy()
                    login_status = 1
                    return(1)

        if user == len(usernames)-1:
            password_not_recognised()

def login_verify_raw(username_entry,password_entry):

    sql_parsing()

    for user in range(len(usernames)):
        if username_entry == usernames[user]:
            if password_entry == passwords[user]:
                if function_server_time_flag(user) == 1:    #success
                    time = server_time()
                    time_year = (expired[user][0] - time[0]) * 365
                    time_month = (expired[user][1] - time[1]) * 30
                    time_days = (expired[user][2] - time[2])
                    time_total = time_year + time_month + time_days
                    account_status = (True,time_total)
                    return(account_status)


    account_status = (False, 0)
    return(account_status)


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("140x70")
    Label(password_not_recog_screen, text="Login or License error").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Deleting popups
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
