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
win.title("Car View")
win.geometry("1050x450")

# Car_Id
car_id = IntVar()
Label(win, text="Car_Id").place(x=20, y=20)
Entry(win, textvariable=car_id, state="readonly").place(x=110, y=20)
# Name_Customer
name_customer = StringVar()
Label(win, text="Name").place(x=20, y=60)
Entry(win, textvariable=name_customer).place(x=110, y=60)
# Family_Customer
family_customer = StringVar()
Label(win, text="Family").place(x=20, y=100)
Entry(win, textvariable=family_customer).place(x=110, y=100)
# Phone_Number
phone_number = StringVar()
Label(win, text="Phone_Num").place(x=20, y=140)
Entry(win, textvariable=phone_number).place(x=110, y=140)
# Plate_Number
plate_number = StringVar()
Label(win, text="Plate_Num").place(x=20, y=180)
Entry(win, textvariable=plate_number).place(x=110, y=180)
# Model
model = StringVar()
Label(win, text="Model").place(x=20, y=220)
Entry(win, textvariable=model).place(x=110, y=220)
# Year
year = IntVar()
Label(win, text="Year").place(x=20, y=260)
Entry(win, textvariable=year).place(x=110, y=260)
# Color
color = StringVar()
Label(win, text="Color").place(x=20, y=300)
Entry(win, textvariable=color).place(x=110, y=300)
# Vin_Number
vin_number = StringVar()
Label(win, text="Vin_Num").place(x=20, y=340)
Entry(win, textvariable=vin_number).place(x=110, y=340)

# Find_By_Plate
find_by_plate = StringVar()
Label(win, text="Find_By_Plate").place(x=260, y=340)
Entry(win, textvariable=find_by_plate).place(x=365, y=340)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=400)
Button(win, text="Edit", width=7, command=edit_click).place(x=100, y=400)
Button(win, text="Remove", width=7, command=remove_click).place(x=180, y=400)
Button(win, text="Find All", width=7, command=find_all_click).place(x=260, y=400)

table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    show="headings"
)

table.heading(1, text="Car Id")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="Phone_Num")
table.heading(5, text="Plate_Num")
table.heading(6, text="Model")
table.heading(7, text="Year")
table.heading(8, text="Color")
table.heading(9, text="Vin_Num")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=50)
table.column(7, width=80)
table.column(8, width=80)
table.column(9, width=100)

table.place(x=260, y=20,height=300)

win.mainloop()
