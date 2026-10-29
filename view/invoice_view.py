import os
import tkinter
from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk

from controller.invoice_controller import InvoiceController


# =========================================================================================================
class InvoiceView:

    def save_click(self):
        status, massage = InvoiceController.save(
            self.invoice_id.get(),
            self.car_id.get(),
            self.parts_cost.get(),
            self.total_service_cost.get(),
            self.discount_amount.get(),
            self.final_amount.get(),
            self.payment_method.get(),
            self.status.get(),
            self.acceptance_timestamp.get()
        )
        if status:
            msg.showinfo("Success", "Invoice saved successfully!")
            self.reset_form()
            self.show_on_table()
        else:
            msg.showerror("Error", "Invoice save failed!")

    def edit_click(self):
        pass

    def remove_click(self):
        pass

    def exit_click(self):
        selected_item = self.table.focus()
        if not selected_item:
            msg.showerror("Error", "Please select a car first!")
            return
        now = datetime.now()
        self.date_exit.set(now.strftime("%Y-%m-%d"))
        self.time_exit.set(now.strftime("%H:%M:%S"))
        self.table.item(selected_item, tags=("exited",))
        msg.showinfo("Success", "Car exited successfully!")

    base_cost = 0

    def select_row(self, event):
        selected_item = self.table.focus()
        if selected_item:
            row_data = self.table.item(selected_item, "values")

            self.car_id.set(row_data[1])
            self.parts_cost.set(row_data[2])
            self.total_service_cost.set(row_data[3])
            self.discount_amount.set(row_data[4])

    def reset_form(self):
        pass

    def clear_table(self):
        pass

    def show_on_table(self):
        pass

    # =========================================================================================================

    def update_final(self, *args):
        try:
            parts = self.parts_cost.get()
        except:
            parts = 0

        try:
            service = self.total_service_cost.get()
        except:
            service = 0

        try:
            discount = self.discount_amount.get()
        except:
            discount = 0

        total = (parts + service) - discount
        self.final_amount.set(total if total >= 0 else 0)

        self.parts_cost.trace_add("write", self.update_final)
        self.total_service_cost.trace_add("write", self.update_final)
        self.discount_amount.trace_add("write", self.update_final)

    # =========================================================================================================

    def __init__(self):
        win = Tk()
        win.title('Invoice View')
        win.geometry('1250x565')

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "invoice_view.jpg")
        car_img = Image.open(image_path)
        resized_img = car_img.resize((1000, 150))
        bg_photo = ImageTk.PhotoImage(resized_img)
        lbl_photo = Label(win, image=bg_photo)
        lbl_photo.image = bg_photo
        lbl_photo.place(x=280, y=400)

        # Invoice_Id
        self.invoice_id = IntVar()
        Label(win, text="Invoice Id").place(x=20, y=20)
        Entry(win, textvariable=self.invoice_id, state="readonly").place(x=130, y=20)
        # Car_Id
        self.car_id = IntVar()
        Label(win, text="Car Id").place(x=20, y=60)
        Entry(win, textvariable=self.car_id, state="readonly").place(x=130, y=60)
        # Parts_Cost
        self.parts_cost = IntVar()
        Label(win, text="Parts Cost").place(x=20, y=100)
        Entry(win, textvariable=self.parts_cost).place(x=130, y=100)

        # Total_Service_Cost
        self.total_service_cost = IntVar()
        Label(win, text="Total Service Cost").place(x=20, y=140)
        Entry(win, textvariable=self.total_service_cost).place(x=130, y=140)
        # Discount_Amount
        self.discount_amount = IntVar()
        Label(win, text="Discount Amount").place(x=20, y=180)
        Entry(win, textvariable=self.discount_amount).place(x=130, y=180)
        # Final_Amount
        self.final_amount = IntVar()
        Label(win, text="Final Amount").place(x=20, y=220)
        Entry(win, textvariable=self.final_amount, state="readonly").place(x=130, y=220)
        # Payment_Method
        self.payment_method = StringVar()
        Label(win, text="Payment").place(x=20, y=260)
        combo_payment = ttk.Combobox(win, width=17, textvariable=self.payment_method, state="readonly")
        combo_payment["values"] = (
            "Cash",
            "CreditCard",
            "Pos",
            "Transfer"
        )
        combo_payment.current(0)
        combo_payment.place(x=130, y=260)

        # Date_Exit
        self.date_exit = StringVar()
        Label(win, text="Date Exit").place(x=20, y=300)
        Entry(win, textvariable=self.date_exit, state="readonly").place(x=130, y=300)
        # Time_Exit
        self.time_exit = StringVar()
        Label(win, text="Time Exit").place(x=20, y=340)
        Entry(win, textvariable=self.time_exit, state="readonly").place(x=130, y=340)

        # Status
        self.status = StringVar()
        Label(win, text="Status").place(x=20, y=380)
        combo_status = ttk.Combobox(win, width=17, textvariable=self.status, state="readonly")
        combo_status["values"] = (
            "in_progress",
            "completed",
            "exited"
        )
        combo_status.current(0)
        combo_status.place(x=130, y=380)

        # Acceptance Timestamp
        self.acceptance_timestamp = StringVar()
        Label(win, text="Acceptance Time").place(x=20, y=420)
        Entry(win, textvariable=self.acceptance_timestamp, state="readonly").place(x=130, y=420)

        # Find_By_Date
        self.find_by_date = StringVar()
        Label(win, text=" Start Date").place(x=365, y=20)
        Entry(win, textvariable=self.find_by_date).place(x=430, y=20)

        # Find_By_Date
        self.end_date = StringVar()
        Label(win, text=" End Date").place(x=575, y=20)
        Entry(win, textvariable=self.end_date).place(x=640, y=20)

        # =========================================================================================================

        # =========================================================================================================

        Button(win, text="Save", width=7, command=self.save_click).place(x=20, y=480)
        Button(win, text="Edit", width=7, command=self.edit_click).place(x=100, y=480)
        Button(win, text="Remove", width=7, command=self.remove_click).place(x=180, y=480)
        Button(win, text="Exit", width=7, command=self.exit_click).place(x=100, y=515)
        Button(win, text="New", width=7, command=self.reset_form).place(x=20, y=515)

        # =========================================================================================================
        self.table = ttk.Treeview(
            win,
            columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
            show="headings"
        )
        self.table.heading(1, text="Invoice Id")
        self.table.heading(2, text="Car Id")
        self.table.heading(3, text="Parts Cost")
        self.table.heading(4, text="Total Cost")
        self.table.heading(5, text="Discount Amount")
        self.table.heading(6, text="Final Amount")

        self.table.heading(7, text="Payment")
        self.table.heading(8, text="Date Exit")
        self.table.heading(9, text="Time Exit")
        self.table.heading(10, text="status")
        self.table.heading(11, text="Accept Time")

        self.table.column(1, width=80)
        self.table.column(2, width=80)
        self.table.column(3, width=80)
        self.table.column(4, width=110)
        self.table.column(5, width=100)
        self.table.column(6, width=110)
        self.table.column(7, width=80)
        self.table.column(8, width=80)
        self.table.column(9, width=80)
        self.table.column(10, width=80)
        self.table.column(11, width=80)

        self.table.place(x=280, y=60, height=340)
        self.table.bind("<<TreeviewSelect>>", self.select_row)
        # =========================================================================================================
        self.table.tag_configure("in_progress", background="yellow")
        self.table.tag_configure("completed", background="green")
        self.table.tag_configure("exited", background="red")

        # clean table

        # for invoice in invoice_list:
        #     table.insert("", "end", values=invoice.to_tuple(), tags=invoice.status)

        win.mainloop()


ui = InvoiceView()
