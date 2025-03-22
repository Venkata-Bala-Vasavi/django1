import tkinter as tk
from tkinter import messagebox
def login():
    userid = userentry.get()
    password = pasentry.get()
    if userid == "admin" and password == "password":
        messagebox.showinfo("login sucessful",f"Welcome, {userid}!")
    else:
        messagebox.showerror("error","Login Failed")
root = tk.Tk()
root.title("Login Form")
root.geometry("400x400")
username = tk.Label(root, text="Username:")
username.pack()
userentry = tk.Entry(root)
userentry.pack()
pas= tk.Label(root, text="Password:")
pas.pack()
pasentry = tk.Entry(root, show="*")
pasentry.pack()
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()
root.mainloop()
