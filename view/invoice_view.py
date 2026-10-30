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
        status, message = InvoiceController.save(
            self.car_id.get(),
            self.parts_cost.get(),
            self.total_service_cost.get(),
            self.discount_amount.get(),
            self.payment_method.get(),
            self.status.get(),
        )
        if status:
            msg.showinfo("Success", "Invoice saved successfully!")
            self.reset_form()
            self.show_on_table()
        else:
            msg.showerror("Error", "Invoice save failed!")

    def edit_click(self):
        status, message = InvoiceController.update(
            self.invoice_id.get(),
            self.parts_cost.get(),
            self.total_service_cost.get(),
            self.discount_amount.get(),
            self.payment_method.get(),
            self.status.get(),
        )

        if status:
            msg.showinfo("Success", "Invoice updated successfully!")
            self.reset_form()
            self.show_on_table()
        else:
            msg.showerror("Error", "Invoice update failed!")

    def remove_click(self):
        if msg.askyesno("Remove Invoice", "Do you really want to remove this invoice?"):
            status, message = InvoiceController.delete(self.invoice_id.get())
            if status:
                msg.showinfo("Success", "Invoice removed successfully!")
                self.reset_form()
                self.show_on_table()
            else:
                msg.showerror("Error", "Invoice remove failed!")

    def exit_click(self):
        selected_item = self.table.focus()
        if not selected_item:
            msg.showerror("Error", "Please select a car first!")
            return
        if self.status.get() == "exited":
            msg.showwarning("Warning", "This invoice has already been exited!")
            return
        now = datetime.now()
        self.date_exit.set(now.strftime("%Y-%m-%d"))
        self.time_exit.set(now.strftime("%H:%M:%S"))
        status, message = InvoiceController.register_exit(
            self.invoice_id.get(),
            self.date_exit.get(),
            self.time_exit.get()
        )
        if status:
            msg.showinfo("Success", "Car exited successfully!")
            self.reset_form()
            self.show_on_table()
        else:
            msg.showerror("Error", "Car exited failed!")

    base_cost = 0

    def select_row(self, event=None):
        selected_item = self.table.focus()
        if not selected_item:
            return
        selected_item = self.table.item(selected_item, "values")

        if selected_item:
            self.invoice_id.set(selected_item[0])
            self.car_id.set(selected_item[1])
            self.parts_cost.set(selected_item[2])
            self.total_service_cost.set(selected_item[3])
            self.discount_amount.set(selected_item[4])
            self.final_amount.set(selected_item[5])
            self.payment_method.set(selected_item[6])
            self.date_exit.set(selected_item[7])
            self.time_exit.set(selected_item[8])
            self.status.set(selected_item[9])
            self.acceptance_timestamp.set(selected_item[10])

    def reset_form(self):
        self.invoice_id.set(0)
        self.car_id.set(0)
        self.parts_cost.set(0.0)
        self.total_service_cost.set(0.0)
        self.discount_amount.set(0.0)
        self.final_amount.set(0.0)
        self.payment_method.set("Cash")
        self.date_exit.set("")
        self.time_exit.set("")
        self.status.set("in progress")
        self.acceptance_timestamp.set("")

    def clear_table(self):
        self.table.delete(*self.table.get_children())

    def show_on_table(self):
        self.clear_table()
        status, invoices = InvoiceController.find_all()
        if status and invoices:
            for invoice in invoices:
                self.table.insert('', 'end', values=invoice, tags=(invoice[9],))
    # =========================================================================================================

    def update_final(self, *args):
        try:
            parts = self.parts_cost.get()
        except (ValueError,tkinter.TclError):
            parts = 0

        try:
            service = self.total_service_cost.get()
        except (ValueError,tkinter.TclError):
            service = 0

        try:
            discount = self.discount_amount.get()
        except (ValueError,tkinter.TclError):
            discount = 0

        total = (parts + service) - discount
        self.final_amount.set(max(total, 0))

    # =========================================================================================================

    def __init__(self):
        win = Tk()
        win.title('Invoice View')
        win.geometry('1330x565')

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
        Entry(win, textvariable=self.car_id).place(x=130, y=60)
        # Parts_Cost
        self.parts_cost = DoubleVar()
        Label(win, text="Parts Cost").place(x=20, y=100)
        Entry(win, textvariable=self.parts_cost).place(x=130, y=100)

        # Total_Service_Cost
        self.total_service_cost = DoubleVar()
        Label(win, text="Total Service Cost").place(x=20, y=140)
        Entry(win, textvariable=self.total_service_cost).place(x=130, y=140)
        # Discount_Amount
        self.discount_amount = DoubleVar()
        Label(win, text="Discount Amount").place(x=20, y=180)
        Entry(win, textvariable=self.discount_amount).place(x=130, y=180)
        # Final_Amount
        self.final_amount = DoubleVar()
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
            "in progress",
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
        self.table.column(11, width=150)

        self.table.place(x=280, y=60, height=340)
        self.table.bind("<<TreeviewSelect>>", self.select_row)
        # =========================================================================================================
        self.table.tag_configure("in progress", background="yellow")
        self.table.tag_configure("completed", background="green")
        self.table.tag_configure("exited", background="red")
        self.parts_cost.trace_add("write", self.update_final)
        self.total_service_cost.trace_add("write", self.update_final)
        self.discount_amount.trace_add("write", self.update_final)
        # clean table

        # for invoice in invoice_list:
        #     table.insert("", "end", values=invoice.to_tuple(), tags=invoice.status)
        self.show_on_table()
        win.mainloop()


ui = InvoiceView()
