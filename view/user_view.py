from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from model.user import User
import os


def reset_click():
    user_id.set(0)
    name.set("")
    family.set("")
    national_id.set("")
    phone_number.set("")
    table.selection_remove(table.selection())


def save_click():
    pass


def edit_click():
    pass


def remove_click():
    pass


win = Tk()
win.title("User View")
win.geometry("880x330")

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "welcome_view.jpg")

welcome_img = Image.open(image_path)
resized_img = welcome_img.resize((150, 150))

bg_photo = ImageTk.PhotoImage(resized_img)
lbl_photo = Label(win, image=bg_photo)
lbl_photo.image = bg_photo
lbl_photo.place(x=720, y=60)

# User_ID
user_id = IntVar()
Label(win, text="User ID").place(x=20, y=20)
Entry(win, textvariable=user_id, state="readonly").place(x=100, y=20)
# Name
name = StringVar()
Label(win, text="Name").place(x=20, y=60)
Entry(win, textvariable=name).place(x=100, y=60)
# Family
family = StringVar()
Label(win, text="Family").place(x=20, y=100)
Entry(win, textvariable=family).place(x=100, y=100)
# National_Id
national_id = StringVar()
Label(win, text="National Id").place(x=20, y=140)
Entry(win, textvariable=national_id).place(x=100, y=140)
# Phone_Number
phone_number = StringVar()
Label(win, text="Phone Num").place(x=20, y=180)
Entry(win, textvariable=phone_number).place(x=100, y=180)

# ----------------------------------------------------------------------
"""
username , password از این بخش پروژه حذف شدن ولی بصورت کامنت قرار میگیرن تا بعدا در آپدیت پروژه بتونیم بازهم این 2 مورد رو به پروژه اضافه کنیم
"""
# Username
# username = StringVar()
# Label(win, text="Username").place(x=20, y=220)
# Entry(win, textvariable=username).place(x=100, y=220)
# Password
# -------------------------------------------------------------------------------
# Find_By_Id
find = StringVar()
Label(win, text="Find By Id").place(x=250, y=20)
Entry(win, textvariable=find).place(x=310, y=20)

# Find_By_Family
find_by_family = StringVar()
Label(win, text="Find By Family").place(x=440, y=20)
Entry(win, textvariable=find_by_family).place(x=540, y=20)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=230)
Button(win, text="Edit", width=7, command=edit_click).place(x=100, y=230)
Button(win, text="Remove", width=7, command=remove_click).place(x=180, y=230)

table = ttk.Treeview(
    win,
    column=(1, 2, 3, 4, 5,),
    show='headings'
)

table.heading(1, text="User ID")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="National Id")
table.heading(5, text="Phone Num")
# ---------------------------------------------
# table.heading(6, text="Username")
# table.heading(7, text="Password")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
# -----------------------------------------------------
# table.column(6, width=100)
# table.column(7, width=100)

table.place(x=250, y=60)

win.mainloop()
