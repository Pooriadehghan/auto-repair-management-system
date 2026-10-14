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
win.geometry("1085x335")

car_img = Image.open("car_view.jpg")
resized_img = car_img.resize((280, 250))
bg_photo = ImageTk.PhotoImage(resized_img)
lbl_photo = Label(win, image=bg_photo)
lbl_photo.image = bg_photo
lbl_photo.place(x=785, y=57)




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

# Find_By_Plate
find_by_plate = StringVar()
Label(win, text="Find By Plate").place(x=260, y=20)
Entry(win, textvariable=find_by_plate).place(x=365, y=20)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=280)
Button(win, text="Edit", width=7, command=edit_click).place(x=100, y=280)
Button(win, text="Remove", width=7, command=remove_click).place(x=180, y=280)

table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5, 6),
    show="headings"
)

table.heading(1, text="Car Id")
# table.heading(2, text="Name")
# table.heading(3, text="Family")
# table.heading(4, text="Phone_Num")
table.heading(2, text="Plate Num")
table.heading(3, text="Model")
table.heading(4, text="Year")
table.heading(5, text="Color")
table.heading(6, text="Vin_Num")

table.column(1, width=60)
# table.column(2, width=100)
# table.column(3, width=100)
# table.column(4, width=100)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=80)
table.column(5, width=80)
table.column(6, width=100)

table.place(x=260, y=60, height=250)

win.mainloop()
