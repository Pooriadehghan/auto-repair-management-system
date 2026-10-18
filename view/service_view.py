from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def save_click():
    pass


def edit_click():
    pass


def remove_click():
    pass


# def update_total(*args):
#     try:
#         total = labor_cost.get() + parts_cost.get()
#         calculate_total.set(round(total, 2))
#     except Exception:
#         calculate_total.set(0.0)


win = Tk()
win.title("Service View")
win.geometry("700x350")

# Service_Id
service_id = IntVar()
Label(win, text="Service Id").place(x=20, y=20)
Entry(win, textvariable=service_id, state="readonly").place(x=100, y=20)

# Service_Type
service_type = StringVar()
Label(win, text="Service Type").place(x=20, y=60)
# Entry(win, textvariable=service_type).place(x=100, y=100)
combo_service = ttk.Combobox(win, width=17, textvariable=service_type, state="readonly")
combo_service["values"] = (
    "Car Wash",
    "Pdr",
    "Periodic Service",
    "Repair"
)
combo_service.current(0)
combo_service.place(x=100, y=60)
# Description
description = StringVar()
Label(win, text="Description").place(x=20, y=100)
Entry(win, textvariable=description).place(x=100, y=100)

# Labor_Cost
labor_cost = DoubleVar()
Label(win, text="Labor Cost").place(x=20, y=140)
Entry(win, textvariable=labor_cost).place(x=100, y=140)

# Find_By_Id
find_by_id = IntVar()
Label(win, text="Find By Id").place(x=250, y=20)
Entry(win, textvariable=find_by_id).place(x=315, y=20)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=295)
Button(win, text="Edit", width=7, command=edit_click).place(x=100, y=295)
Button(win, text="Remove", width=7, command=remove_click).place(x=180, y=295)

table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4),
    show="headings"
)

table.heading(1, text="Service_Id")
table.heading(2, text="Service_Type")
table.heading(3, text="Description")
table.heading(4, text="Labor_Cost")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=200)
table.column(4, width=80)

table.place(x=250, y=60, height=260)

win.mainloop()
