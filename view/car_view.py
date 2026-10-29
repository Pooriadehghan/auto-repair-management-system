import os
from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk
from PIL import Image, ImageTk
from controller.car_controller import CarController


class CarView:
    def save_click(self):
        status, massage = CarController.save(
            self.car_id.get(),
            self.plate_number.get(),
            self.model.get(),
            self.year.get(),
            self.color.get(),
            self.vin_number.get(),
            self.owner_national_id.get()
        )
        if status:
            msg.showinfo("Success", "Car Saved")
            self.reset_click()
            self.show_on_table()
        else:
            msg.showerror("Error", "Car Could not be  Saved")

    def edit_click(self):
        status, massage = CarController.update(
            self.car_id.get(),
            self.plate_number.get(),
            self.model.get(),
            self.year.get(),
            self.color.get(),
            self.vin_number.get(),
            self.owner_national_id.get()
        )
        if status:
            msg.showinfo("Success", "Car Edited")
            self.reset_click()
            self.show_on_table()
        else:
            msg.showerror("Error", "Car Could not be  Edited")

    def remove_click(self):
        if msg.askyesno("Remove Car", "Remove Car?"):
            status, massage = CarController.delete(self.car_id.get())
            if status:
                msg.showinfo("Success", "Car Removed")
                self.reset_click()
                self.show_on_table()
            else:
                msg.showerror("Error", "Car Could not be  Removed")

    # ========================================================================
    def select_car(self):
        select_items = self.table.selection()

        if not select_items:
            return
        select_item = self.table.item(select_items[0], "values")

        if not select_item or len(select_item) < 7:
            return

        self.car_id.set(select_item[0])
        self.plate_number.set(select_item[1])
        self.model.set(select_item[2])
        self.year.set(select_item[3])
        self.color.set(select_item[4])
        self.vin_number.set(select_item[5])
        self.owner_national_id.set(select_item[6])

    def reset_click(self):
        self.car_id.set(0)
        self.plate_number.set("")
        self.model.set("")
        self.year.set(0)
        self.color.set("")
        self.vin_number.set("")
        self.owner_national_id.set("")
        self.table.selection_remove(*self.table.selection())

    def clear_table(self):
        self.table.delete(*self.table.get_children())

    def show_on_table(self):
        self.clear_table()
        status, cars = CarController.find_all()
        if status and cars:
            for car in cars:
                self.table.insert('', 'end', values=car)

    # ========================================================================
    def search_by_plate(self):
        car_plate = self.plate_number.get()
        self.clear_table()

        if not car_plate:
            self.show_on_table()
            return
        status, cars = CarController.find_by_plate_number(car_plate)
        print(cars)

        if status and cars:
            self.table.insert('', 'end', values=cars)

    # ========================================================================

    def __init__(self):
        win = Tk()
        win.title("Car View")
        win.geometry("1205x395")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "car_view.jpg")
        car_img = Image.open(image_path)
        resized_img = car_img.resize((280, 250))
        bg_photo = ImageTk.PhotoImage(resized_img)
        lbl_photo = Label(win, image=bg_photo)
        lbl_photo.image = bg_photo
        lbl_photo.place(x=905, y=57)

        # Car_Id
        self.car_id = IntVar()
        Label(win, text="Car Id").place(x=20, y=20)
        Entry(win, textvariable=self.car_id, state="readonly").place(x=110, y=20)
        # Plate_Number
        self.plate_number = StringVar()
        Label(win, text="Plate Num").place(x=20, y=60)
        Entry(win, textvariable=self.plate_number).place(x=110, y=60)
        # Model
        self.model = StringVar()
        Label(win, text="Model").place(x=20, y=100)
        Entry(win, textvariable=self.model).place(x=110, y=100)
        # Year
        self.year = IntVar()
        Label(win, text="Year").place(x=20, y=140)
        Entry(win, textvariable=self.year).place(x=110, y=140)
        # Color
        self.color = StringVar()
        Label(win, text="Color").place(x=20, y=180)
        Entry(win, textvariable=self.color).place(x=110, y=180)
        # Vin_Number
        self.vin_number = StringVar()
        Label(win, text="Vin Num").place(x=20, y=220)
        Entry(win, textvariable=self.vin_number).place(x=110, y=220)

        # Owner National id
        self.owner_national_id = StringVar()
        Label(win, text="Owner Nat ID").place(x=20, y=260)
        Entry(win, textvariable=self.owner_national_id).place(x=110, y=260)

        # Find_By_Plate
        self.find_by_plate = StringVar()
        Label(win, text="Find By Plate").place(x=260, y=20)
        self.find_entry = Entry(win, textvariable=self.find_by_plate)
        self.find_entry.place(x=365, y=20)

        Button(win, text="Save", width=7, command=self.save_click).place(x=20, y=310)
        Button(win, text="Edit", width=7, command=self.edit_click).place(x=100, y=310)
        Button(win, text="Remove", width=7, command=self.remove_click).place(x=180, y=310)
        Button(win, text="New", width=7, command=self.reset_click).place(x=20, y=350)
        self.table = ttk.Treeview(
            win,
            columns=(1, 2, 3, 4, 5, 6, 7),
            show="headings"
        )

        self.table.heading(1, text="Car Id")
        self.table.heading(2, text="Plate Num")
        self.table.heading(3, text="Model")
        self.table.heading(4, text="Year")
        self.table.heading(5, text="Color")
        self.table.heading(6, text="Vin Num")
        self.table.heading(7, text="Owner Nat Id")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=80)
        self.table.column(5, width=80)
        self.table.column(6, width=120)
        self.table.column(7, width=100)

        self.table.place(x=260, y=60, height=280)

        self.table.bind("<<TreeviewSelect>>", self.select_car)
        self.find_entry.bind("<KeyRelease>", self.search_by_plate)
        self.show_on_table()

        win.mainloop()


ui = CarView()
