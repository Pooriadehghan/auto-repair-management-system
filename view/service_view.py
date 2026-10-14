from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def save_click():
    pass


def edit_click():
    pass


def remove_click():
    pass


def update_total(*args):
    try:
        total = labor_cost.get() + parts_cost.get()
        calculate_total.set(round(total, 2))
    except Exception:
        calculate_total.set(0.0)


win = Tk()
win.title("Service View")
win.geometry("960x390")

# Service_Id
service_id = IntVar()
Label(win, text="ServiceId").place(x=20, y=20)
Entry(win, textvariable=service_id, state="readonly").place(x=100, y=20)

# Car_Id
car_id = IntVar()
Label(win, text="Car Id").place(x=20, y=60)
Entry(win, textvariable=car_id, state="readonly").place(x=100, y=60)

# Service_Type
service_type = StringVar()
Label(win, text="Service Type").place(x=20, y=100)
# Entry(win, textvariable=service_type).place(x=100, y=100)
combo_service = ttk.Combobox(win, width=17, textvariable=service_type, state="readonly")
combo_service["values"] = (
    "Car Wash",
    "Pdr",
    "Periodic Service",
    "Repair"
)
combo_service.current(0)
combo_service.place(x=100, y=100)
# Description
description = StringVar()
Label(win, text="Description").place(x=20, y=140)
Entry(win, textvariable=description).place(x=100, y=140)

# Labor_Cost
labor_cost = DoubleVar()
Label(win, text="Labor Cost").place(x=20, y=180)
Entry(win, textvariable=labor_cost).place(x=100, y=180)

# Parts_Cost
parts_cost = DoubleVar()
Label(win, text="Parts Cost").place(x=20, y=220)
Entry(win, textvariable=parts_cost).place(x=100, y=220)

# Acceptance_Date
date = StringVar()
Label(win, text="Date").place(x=20, y=260)
Entry(win, textvariable=date, state="readonly").place(x=100, y=260)

# Acceptance_Time
time = StringVar()
Label(win, text="Time").place(x=20, y=300)
Entry(win, textvariable=time, state="readonly").place(x=100, y=300)

# Find_By_Id
find_by_id = IntVar()
Label(win, text="Find By Id").place(x=250, y=20)
Entry(win, textvariable=find_by_id).place(x=315, y=20)

# Calculate Total
calculate_total = DoubleVar()
Label(win, text="Calculate Total").place(x=450, y=20)
Entry(win, textvariable=calculate_total, state="readonly").place(x=550, y=20)

labor_cost.trace_add("write", update_total)
parts_cost.trace_add("write", update_total)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=340)
Button(win, text="Edit", width=7, command=edit_click).place(x=100, y=340)
Button(win, text="Remove", width=7, command=remove_click).place(x=180, y=340)

table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5, 6, 7, 8),
    show="headings"
)

table.heading(1, text="Service_Id")
table.heading(2, text="Car_Id")
table.heading(3, text="Service_Type")
table.heading(4, text="Description")
table.heading(5, text="Labor_Cost")
table.heading(6, text="Parts_Cost")
table.heading(7, text="Date")
table.heading(8, text="Time")

table.column(1, width=60)
table.column(2, width=60)
table.column(3, width=100)
table.column(4, width=150)
table.column(5, width=80)
table.column(6, width=80)
table.column(7, width=80)
table.column(8, width=80)

table.place(x=250, y=60, height=260)

win.mainloop()
