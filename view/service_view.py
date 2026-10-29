from controller.service_controller import ServiceController
from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk


class ServiceView:

    def save_click(self):
        status, massage = ServiceController.save(
            self.service_id.get(),
            self.service_type.get(),
            self.description.get(),
            self.labor_cost.get()

        )
        if status:
            msg.showinfo("Success", "Service Saved")
            self.reset_click()
            self.show_on_table()
        else:
            msg.showerror("Error", "Service Could not be Saved")

    def edit_click(self):
        status, massage = ServiceController.update(
            self.service_id.get(),
            self.service_type.get(),
            self.description.get(),
            self.labor_cost.get()

        )
        if status:
            msg.showinfo("Success", "Service Updated")
            self.reset_click()
            self.show_on_table()
        else:
            msg.showerror("Error", "Service Could not be Updated")

    def remove_click(self):
        if msg.askyesno("Remove Service", "Remove Service?"):
            status, massage = ServiceController.delete(self.service_id.get())
            if status:
                msg.showinfo("Success", "Service Removed")
                self.reset_click()
                self.show_on_table()
            else:
                msg.showerror("Error", "Service Could not be Removed")

    # ========================================================================================================
    def select_service(self):
        select_items = self.table.selection()

        if not select_items:
            return

        select_item = self.table.item(select_items[0], "values")

        if not select_item or len(select_item) < 4:
            return

        self.service_id.set(select_item[0])
        self.service_type.set(select_item[1])
        self.description.set(select_item[2])
        self.labor_cost.set(select_item[3])

    def reset_click(self):
        self.service_id.set(0)
        self.service_type.set("Car Wash")
        self.description.set("")
        self.labor_cost.set(0.0)
        self.table.selection_remove(*self.table.selection())

    def clear_table(self):
        self.table.delete(*self.table.get_children())

    def show_on_table(self):
        self.clear_table()
        status, services = ServiceController.find_all()
        if status and services:
            for service in services:
                self.table.insert('', 'end', values=service)

    # ========================================================================================================
    def search_by_id(self):
        service_id = self.find_by_id.get()
        self.clear_table()

        if not service_id:
            self.show_on_table()
            return

        status, services = ServiceController.find_by_id(service_id)
        print(services)

        if status and services:
            self.table.insert('', 'end', values=services)

    def __init__(self):
        win = Tk()
        win.title("Service View")
        win.geometry("700x350")

        # Service_Id
        self.service_id = IntVar()
        Label(win, text="Service Id").place(x=20, y=20)
        Entry(win, textvariable=self.service_id, state="readonly").place(x=100, y=20)

        # Service_Type
        self.service_type = StringVar()
        Label(win, text="Service Type").place(x=20, y=60)
        # Entry(win, textvariable=service_type).place(x=100, y=100)
        combo_service = ttk.Combobox(win, width=17, textvariable=self.service_type, state="readonly")
        combo_service["values"] = (
            "Car Wash",
            "Pdr",
            "Periodic Service",
            "Repair"
        )
        combo_service.current(0)
        combo_service.place(x=100, y=60)
        # Description
        self.description = StringVar()
        Label(win, text="Description").place(x=20, y=100)
        Entry(win, textvariable=self.description).place(x=100, y=100)

        # Labor_Cost
        self.labor_cost = DoubleVar()
        Label(win, text="Labor Cost").place(x=20, y=140)
        Entry(win, textvariable=self.labor_cost).place(x=100, y=140)

        # Find_By_Id
        self.find_by_id = IntVar()
        Label(win, text="Find By Id").place(x=250, y=20)
        self.find_entry = Entry(win, textvariable=self.find_by_id)
        self.find_entry.place(x=315, y=20)

        Button(win, text="Save", width=7, command=self.save_click).place(x=20, y=295)
        Button(win, text="Edit", width=7, command=self.edit_click).place(x=100, y=295)
        Button(win, text="Remove", width=7, command=self.remove_click).place(x=180, y=295)
        Button(win, text="New", width=7, command=self.reset_click).place(x=20, y=265)

        self.table = ttk.Treeview(
            win,
            columns=(1, 2, 3, 4),
            show="headings"
        )
        self.show_on_table()

        self.table.heading(1, text="Service_Id")
        self.table.heading(2, text="Service_Type")
        self.table.heading(3, text="Description")
        self.table.heading(4, text="Labor_Cost")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=200)
        self.table.column(4, width=80)

        self.table.place(x=250, y=60, height=260)

        self.table.bind("<<TreeviewSelect>>", self.select_service)
        self.find_entry.bind("<KeyRelease>", self.search_by_id)
        self.show_on_table()

        win.mainloop()


ui = ServiceView()
