import tkinter
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
win.title('Invoice View')
win.geometry('930x430')

# Invoice_Id
invoice_id = IntVar()
Label(win, text="Invoice_Id").place(x=20, y=20)
Entry(win, textvariable=invoice_id, state="readonly").place(x=130, y=20)
# Car_Id
car_id = IntVar()
Label(win, text="Car_Id").place(x=20, y=60)
Entry(win, textvariable=car_id, state="readonly").place(x=130, y=60)
# Total_Service_Cost
total_service_cost = IntVar()
Label(win, text="Total_Service_Cost").place(x=20, y=100)
Entry(win, textvariable=total_service_cost).place(x=130, y=100)
# Discount_Amount
discount_amount = IntVar()
Label(win, text="Discount_Amount").place(x=20, y=140)
Entry(win, textvariable=discount_amount).place(x=130, y=140)
# Final_Amount
final_amount = IntVar()
Label(win, text="Final_Amount").place(x=20, y=180)
Entry(win, textvariable=final_amount).place(x=130, y=180)
# Payment_Method
payment_method = StringVar()
Label(win, text="Payment").place(x=20, y=220)
combo_payment = ttk.Combobox(win, width=17, textvariable=payment_method, state="readonly")
combo_payment["values"] = (
    "Cash",
    "CreditCard",
    "Pos",
    "Transfer"
)
combo_payment.current(0)
combo_payment.place(x=130, y=220)
# Date_Exit
date_exit = StringVar()
Label(win, text="Date_Exit").place(x=20, y=260)
Entry(win, textvariable=date_exit, state="readonly").place(x=130, y=260)
# Time_Exit
time_exit = StringVar()
Label(win, text="Time_Exit").place(x=20, y=300)
Entry(win, textvariable=time_exit, state="readonly").place(x=130, y=300)
# Find_By_Date
find_by_date = IntVar()
Label(win, text="Find_By_Date").place(x=20, y=340)
Entry(win, textvariable=find_by_date).place(x=130, y=340)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=380)
Button(win, text="Edit", width=7, command=edit_click).place(x=100, y=380)
Button(win, text="Remove", width=7, command=remove_click).place(x=180, y=380)

# Find All
Button(win, text="Find All", width=7, command=find_all_click).place(x=260, y=380)

table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5, 6, 7, 8),
    show="headings"
)

table.heading(1, text="Service_Id")
table.heading(2, text="Car_Id")
table.heading(3, text="Total_Cost")
table.heading(4, text="Discount_Amount")
table.heading(5, text="Final_Amount")
table.heading(6, text="Payment")
table.heading(7, text="Date")
table.heading(8, text="Time")

table.column(1, width=80)
table.column(2, width=80)
table.column(3, width=80)
table.column(4, width=80)
table.column(5, width=80)
table.column(6, width=100)
table.column(7, width=80)
table.column(8, width=80)

table.place(x=260, y=20, height=340)

win.mainloop()
