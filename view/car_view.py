import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk


def reset_form():
    car_id.set(0)
    plate_number.set("")
    model.set("")
    year.set(0)
    color.set("")
    vin_number.set("")
    table.selection_remove(table.selection())


def save_click():
    pass


def edit_click():
    pass


def remove_click():
    pass


win = Tk()
win.title("Car View")
win.geometry("1185x370")

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "car_view.jpg")
car_img = Image.open(image_path)
resized_img = car_img.resize((280, 250))
bg_photo = ImageTk.PhotoImage(resized_img)
lbl_photo = Label(win, image=bg_photo)
lbl_photo.image = bg_photo
lbl_photo.place(x=885, y=57)

# Car_Id
car_id = IntVar()
Label(win, text="Car Id").place(x=20, y=20)
Entry(win, textvariable=car_id, state="readonly").place(x=110, y=20)
# Plate_Number
plate_number = StringVar()
Label(win, text="Plate Num").place(x=20, y=60)
Entry(win, textvariable=plate_number).place(x=110, y=60)
# Model
model = StringVar()
Label(win, text="Model").place(x=20, y=100)
Entry(win, textvariable=model).place(x=110, y=100)
# Year
year = IntVar()
Label(win, text="Year").place(x=20, y=140)
Entry(win, textvariable=year).place(x=110, y=140)
# Color
color = StringVar()
Label(win, text="Color").place(x=20, y=180)
Entry(win, textvariable=color).place(x=110, y=180)
# Vin_Number
vin_number = StringVar()
Label(win, text="Vin Num").place(x=20, y=220)
Entry(win, textvariable=vin_number).place(x=110, y=220)

# Owner National Id
owner_national_id = StringVar()
Label(win, text="Owner Nat ID").place(x=20, y=260)
Entry(win, textvariable=owner_national_id).place(x=110, y=260)

# Find_By_Plate
find_by_plate = StringVar()
Label(win, text="Find By Plate").place(x=260, y=20)
Entry(win, textvariable=find_by_plate).place(x=365, y=20)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=310)
Button(win, text="Edit", width=7, command=edit_click).place(x=100, y=310)
Button(win, text="Remove", width=7, command=remove_click).place(x=180, y=310)

table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5, 6, 7),
    show="headings"
)

table.heading(1, text="Car Id")
table.heading(2, text="Plate Num")
table.heading(3, text="Model")
table.heading(4, text="Year")
table.heading(5, text="Color")
table.heading(6, text="Vin Num")
table.heading(7, text="Owner Nat Id")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=80)
table.column(5, width=80)
table.column(6, width=100)
table.column(7, width=100)

table.place(x=260, y=60, height=280)

win.mainloop()
