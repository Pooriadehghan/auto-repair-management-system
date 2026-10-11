from mailcap import show
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def save_click():
    pass
def edit_click():
    pass
def remove_click():
    pass
def calculate_total_click():
    pass

win=Tk()
win.title("Service View")
win.geometry("960x390")


# Service_Id
service_id=IntVar()
Label(win,text="Service_Id").place(x=20,y=20)
Entry(win,textvariable=service_id,state="readonly").place(x=90,y=20)

# Car_Id
car_id=IntVar()
Label(win,text="Car_Id").place(x=20,y=60)
Entry(win,textvariable=car_id,state="readonly").place(x=90,y=60)

# Service_Type
service_type=StringVar()
Label(win,text="Service_Type").place(x=20,y=100)
Entry(win,textvariable=service_type).place(x=90,y=100)

# Description
description=StringVar()
Label(win,text="Description").place(x=20,y=140)
Entry(win,textvariable=description).place(x=90,y=140)

# Labor_Cost
labor_cost=DoubleVar()
Label(win,text="Labor_Cost").place(x=20,y=180)
Entry(win,textvariable=labor_cost).place(x=90,y=180)

# Parts_Cost
parts_cost=DoubleVar()
Label(win,text="Parts_Cost").place(x=20,y=220)
Entry(win,textvariable=parts_cost).place(x=90,y=220)

# Acceptance_Date
date=StringVar()
Label(win,text="Date").place(x=20,y=260)
Entry(win,textvariable=date,state="readonly").place(x=90,y=260)

# Acceptance_Time
time=StringVar()
Label(win,text="Time").place(x=20,y=300)
Entry(win,textvariable=time,state="readonly").place(x=90,y=300)


#Find_By_Id
find_by_id=IntVar()
Label(win,text="Find_By_Id").place(x=250,y=300)
Entry(win,textvariable=find_by_id).place(x=315,y=300)


Button(win, text="Save", width=7, command=save_click).place(x=20, y=340)
Button(win, text="Edit", width=7, command=edit_click).place(x=100, y=340)
Button(win, text="Delete", width=7, command=remove_click).place(x=180, y=340)
Button(win,text="Calculate Total",width=14,command=calculate_total_click).place(x=260, y=340)


table=ttk.Treeview(
    win,
    columns=(1,2,3,4,5,6,7,8),
    show="headings"
)

table.heading(1,text="Service_Id")
table.heading(2,text="Car_Id")
table.heading(3,text="Service_Type")
table.heading(4,text="Description")
table.heading(5,text="Labor_Cost")
table.heading(6,text="Parts_Cost")
table.heading(7,text="Date")
table.heading(8,text="Time")

table.column(1,width=60)
table.column(2,width=60)
table.column(3,width=100)
table.column(4,width=150)
table.column(5,width=80)
table.column(6,width=80)
table.column(7,width=80)
table.column(8,width=80)

table.place(x=250,y=20)

win.mainloop()