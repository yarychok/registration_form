from tkinter import *
import os

# First window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("800x600")
    main_screen.title("Account Login")
    Label(text="Hello there!").pack()
    Label(text="").pack()
    Button(text="Login", command=login).pack()
    Label(text="").pack()
    Button(text="Register", command=register).pack()
    main_screen.mainloop()

# Registration form
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("800x600")

    global name
    global username
    global password
    global username_entry
    global password_entry
    global name_entry

    name = StringVar()
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Enter details below!").pack()
    Label(register_screen, text="").pack()
    name_lable = Label(register_screen, text="Name")
    name_lable.pack()
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()
    username_lable = Label(register_screen, text="Username")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", command=register_user).pack()

# Login form
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("800x600")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", command=login_verify).pack()

# Function that adding info about users
def register_user():
    name_info = name.get()
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "a")
    file.write(name_info + "\n")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    name_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", command=logged_user()).pack()

# Verifying info about user, that want to sign in
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Valid info
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="To main menu", command=logged_user).pack()

# Main Menu
def logged_user():
    global logged_user_screen
    logged_user_screen = Toplevel(main_screen)
    logged_user_screen.title("Main menu")
    logged_user_screen.geometry("800x600")
    Button(logged_user_screen, text="Add new user")     # command=add_new_user).pack()
    Button(logged_user_screen, text="Edit user")        # command=edit_user.pack()
    Button(logged_user_screen, text="Delete user")      # command=delete_user.pack()
    Button(logged_user_screen, text="Exit")             # command=exit()

# Invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Whoops")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Invalid info
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Whoops")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

main_account_screen()


