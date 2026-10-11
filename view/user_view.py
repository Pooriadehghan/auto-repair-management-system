from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def save_click():
    pass


def edit_click():
    pass


def remove_click():
    pass


def find_all_click():
    pass


win = Tk()
win.title("User View")
win.geometry("980x400")

# User_ID
user_id = IntVar()
Label(win, text="User_ID").place(x=20, y=20)
Entry(win, textvariable=user_id, state="readonly").place(x=90, y=20)
# Name
name = StringVar()
Label(win, text="Name").place(x=20, y=60)
Entry(win, textvariable=name).place(x=90, y=60)
# Family
family = StringVar()
Label(win, text="Family").place(x=20, y=100)
Entry(win, textvariable=family).place(x=90, y=100)
# National_Id
national_id = IntVar()
Label(win, text="National_Id").place(x=20, y=140)
Entry(win, textvariable=national_id).place(x=90, y=140)
# Phone_Number
phone_number = StringVar()
Label(win, text="Phone_Num").place(x=20, y=180)
Entry(win, textvariable=phone_number).place(x=90, y=180)
# Username
username = StringVar()
Label(win, text="Username").place(x=20, y=220)
Entry(win, textvariable=username).place(x=90, y=220)
# Password
password = StringVar()
Label(win, text="Password").place(x=20, y=260)
Entry(win, textvariable=password).place(x=90, y=260)
# Role
role = StringVar()
Label(win, text="Role").place(x=20, y=300)
Radiobutton(win, text="Admin", variable=role, value="Admin").place(x=75, y=300)
Radiobutton(win, text="Manager", variable=role, value="Manager").place(x=135, y=300)
Radiobutton(win, text="Operator", variable=role, value="Operator").place(x=210, y=300)

# Find_By_Id
find = StringVar()
Label(win, text="Find By Id").place(x=250, y=260)
Entry(win, textvariable=find).place(x=310, y=260)

# Find All
Button(win, text="Find All", width=7, command=find_all_click).place(x=260, y=340)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=340)
Button(win, text="Edit", width=7, command=edit_click).place(x=100, y=340)
Button(win, text="Remove", width=7, command=remove_click).place(x=180, y=340)

table = ttk.Treeview(
    win,
    column=(1, 2, 3, 4, 5, 6, 7, 8),
    show='headings',
)

table.heading(1, text="User ID")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="National Id")
table.heading(5, text="Phone Num")
table.heading(6, text="Username")
table.heading(7, text="Password")
table.heading(8, text="Role")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=80)
table.column(5, width=80)
table.column(6, width=100)
table.column(7, width=100)
table.column(8, width=80)

table.place(x=250, y=20)

win.mainloop()
