import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


# =========================================================================================================

def save_click():
    selected_item = table.focus()
    if not selected_item:
        messagebox.showerror("Error", "Please select a car first!")
        return

    table.item(selected_item, tags=("completed",))
    messagebox.showinfo("Success", "Invoice registered successfully!")


def reset_form():
    pass


def edit_click():
    pass


def remove_click():
    pass


def exit_click():
    selected_item = table.focus()
    if not selected_item:
        messagebox.showerror("Error", "Please select a car first!")
        return
    now = datetime.now()
    date_exit.set(now.strftime("%Y-%m-%d"))
    time_exit.set(now.strftime("%H:%M:%S"))
    table.item(selected_item, tags=("exited",))
    messagebox.showinfo("Success", "Car exited successfully!")


base_cost = 0


def select_row(event):
    selected_item = table.focus()
    if selected_item:
        row_data = table.item(selected_item, "values")

        car_id.set(row_data[1])
        parts_cost.set(row_data[2])
        total_service_cost.set(row_data[3])
        discount_amount.set(row_data[4])


# =========================================================================================================


win = Tk()
win.title('Invoice View')
win.geometry('1250x580')

# Invoice_Id
invoice_id = IntVar()
Label(win, text="Invoice Id").place(x=20, y=20)
Entry(win, textvariable=invoice_id, state="readonly").place(x=130, y=20)
# Car_Id
car_id = IntVar()
Label(win, text="Car Id").place(x=20, y=60)
Entry(win, textvariable=car_id, state="readonly").place(x=130, y=60)
# Parts_Cost
parts_cost = IntVar()
Label(win, text="Parts Cost").place(x=20, y=100)
Entry(win, textvariable=parts_cost).place(x=130, y=100)

# Total_Service_Cost
total_service_cost = IntVar()
Label(win, text="Total Service Cost").place(x=20, y=140)
Entry(win, textvariable=total_service_cost).place(x=130, y=140)
# Discount_Amount
discount_amount = IntVar()
Label(win, text="Discount Amount").place(x=20, y=180)
Entry(win, textvariable=discount_amount).place(x=130, y=180)
# Final_Amount
final_amount = IntVar()
Label(win, text="Final Amount").place(x=20, y=220)
Entry(win, textvariable=final_amount, state="readonly").place(x=130, y=220)
# Payment_Method
payment_method = StringVar()
Label(win, text="Payment").place(x=20, y=260)
combo_payment = ttk.Combobox(win, width=17, textvariable=payment_method, state="readonly")
combo_payment["values"] = (
    "Cash",
    "CreditCard",
    "Pos",
    "Transfer"
)
combo_payment.current(0)
combo_payment.place(x=130, y=260)

# Date_Exit
date_exit = StringVar()
Label(win, text="Date Exit").place(x=20, y=300)
Entry(win, textvariable=date_exit, state="readonly").place(x=130, y=300)
# Time_Exit
time_exit = StringVar()
Label(win, text="Time Exit").place(x=20, y=340)
Entry(win, textvariable=time_exit, state="readonly").place(x=130, y=340)

# Status
status = StringVar()
Label(win, text="Status").place(x=20, y=380)
combo_status = ttk.Combobox(win, width=17, textvariable=status, state="readonly")
combo_status["values"] = (
    "in_progress",
    "completed",
    "exited"
)
combo_status.current(0)
combo_status.place(x=130, y=380)

# Acceptance Timestamp
acceptance_timestamp = StringVar()
Label(win, text="Acceptance Time").place(x=20, y=420)
Entry(win, textvariable=acceptance_timestamp, state="readonly").place(x=130, y=420)

# Find_By_Date
find_by_date = StringVar()
Label(win, text=" Start Date").place(x=365, y=20)
Entry(win, textvariable=find_by_date).place(x=430, y=20)

# Find_By_Date
end_date = StringVar()
Label(win, text=" End Date").place(x=575, y=20)
Entry(win, textvariable=end_date).place(x=640, y=20)


# =========================================================================================================
def update_final(*args):
    try:
        parts = parts_cost.get()
    except:
        parts = 0

    try:
        service = total_service_cost.get()
    except:
        service = 0

    try:
        discount = discount_amount.get()
    except:
        discount = 0

    total = (parts + service) - discount
    final_amount.set(total if total >= 0 else 0)


parts_cost.trace_add("write", update_final)
total_service_cost.trace_add("write", update_final)
discount_amount.trace_add("write", update_final)
# =========================================================================================================

Button(win, text="Save", width=7, command=save_click).place(x=20, y=480)
Button(win, text="Edit", width=7, command=edit_click).place(x=100, y=480)
Button(win, text="Remove", width=7, command=remove_click).place(x=180, y=480)
Button(win, text="Exit", width=7, command=exit_click).place(x=260, y=480)

# =========================================================================================================
table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
    show="headings"
)
table.heading(1, text="Invoice Id")
table.heading(2, text="Car Id")
table.heading(3, text="Parts Cost")
table.heading(4, text="Total Cost")
table.heading(5, text="Discount Amount")
table.heading(6, text="Final Amount")
table.heading(7, text="Payment")
table.heading(8, text="Date Exit")
table.heading(9, text="Time Exit")
table.heading(10, text="status")
table.heading(11, text="Accept Time")

table.column(1, width=80)
table.column(2, width=80)
table.column(3, width=80)
table.column(4, width=110)
table.column(5, width=100)
table.column(6, width=110)
table.column(7, width=80)
table.column(8, width=80)
table.column(9, width=80)
table.column(10, width=80)
table.column(11, width=80)

table.place(x=280, y=60, height=340)
table.bind("<<TreeviewSelect>>", select_row)
# =========================================================================================================
table.tag_configure("in_progress", background="yellow")
table.tag_configure("completed", background="green")
table.tag_configure("exited", background="red")

# clean table
# for invoice in invoice_list:
#     table.insert("", "end", values=invoice.to_tuple(), tags=invoice.status)

win.mainloop()
