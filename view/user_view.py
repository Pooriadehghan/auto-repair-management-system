from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk
from PIL import Image, ImageTk
import os
from controller.user_controller import UserController


class UserView:

    def save_click(self):
        status, message = UserController.save(
            self.user_id.get(),
            self.name.get(),
            self.family.get(),
            self.national_id.get(),
            self.phone_number.get()
        )
        if status:
            msg.showinfo("Success", "User saved")
            self.reset_click()
            self.show_on_table()
        else:
            msg.showerror("Error", "User could not be saved")

    def edit_click(self):
        status, massage = UserController.update(
            self.user_id.get(),
            self.name.get(),
            self.family.get(),
            self.national_id.get(),
            self.phone_number.get())
        if status:
            msg.showinfo("Success", "User updated"),
            self.reset_click()
            self.show_on_table()
        else:
            msg.showerror("Error", "User could not be updated")

    def remove_click(self):
        if msg.askyesno("Remove User", "Are you sure you want to remove this user?"):
            status, massage = UserController.delete(self.user_id.get())
            if status:
                msg.showinfo("Success", "User removed")
                self.reset_click()
                self.show_on_table()
            else:
                msg.showerror("Error", "User could not be removed")

    def reset_click(self):
        self.user_id.set(0)
        self.name.set("")
        self.family.set("")
        self.national_id.set("")
        self.phone_number.set("")
        self.table.selection_remove(*self.table.selection())

    def select_product(self, event_info):
        selected_items = self.table.selection()

        if not selected_items:
            return

        select_item = self.table.item(selected_items[0], "values")

        if not select_item or len(select_item) < 5:
            return

        self.user_id.set(int(select_item[0]))
        self.name.set(select_item[1])
        self.family.set(select_item[2])
        self.national_id.set(select_item[3])
        self.phone_number.set(select_item[4])

    def clear_table(self):
        self.table.delete(*self.table.get_children())

    def show_on_table(self):
        self.clear_table()
        status, users = UserController.find_all()
        if status and users:
            for user in users:
                self.table.insert('', 'end', values=user)

    # ========================================================================================
    def search_by_id(self, event):
        user_id = self.find_by_id.get().strip()

        self.clear_table()

        if not user_id:
            self.show_on_table()
            return

        status, user = UserController.find_by_id(user_id)
        print(user)

        if status and user:
            self.table.insert("", "end", values=user)

    # ========================================================================================
    def search_by_national_id(self, event):
        national_id = self.find_by_national_id.get().strip()

        self.clear_table()

        if not national_id:
            self.show_on_table()
            return
        status, user = UserController.find_by_national_id(national_id)
        if status and user:
            self.table.insert("", "end", values=user)

    def __init__(self):

        win = Tk()
        win.title("User View")
        win.geometry("980x330")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "welcome_view.jpg")

        welcome_img = Image.open(image_path)
        resized_img = welcome_img.resize((150, 150))

        bg_photo = ImageTk.PhotoImage(resized_img)
        lbl_photo = Label(win, image=bg_photo)
        lbl_photo.image = bg_photo
        lbl_photo.place(x=820, y=60)

        # User_ID
        self.user_id = IntVar()
        Label(win, text="User ID").place(x=20, y=20)
        Entry(win, textvariable=self.user_id, state="readonly").place(x=100, y=20)
        # Name
        self.name = StringVar()
        Label(win, text="Name").place(x=20, y=60)
        Entry(win, textvariable=self.name).place(x=100, y=60)
        # Family
        self.family = StringVar()
        Label(win, text="Family").place(x=20, y=100)
        Entry(win, textvariable=self.family).place(x=100, y=100)
        # National_Id
        self.national_id = StringVar()
        Label(win, text="National Id").place(x=20, y=140)
        Entry(win, textvariable=self.national_id).place(x=100, y=140)
        # Phone_Number
        self.phone_number = StringVar()
        Label(win, text="Phone Num").place(x=20, y=180)
        Entry(win, textvariable=self.phone_number).place(x=100, y=180)

        # Find_By_Id
        self.find_by_id = StringVar()
        Label(win, text="Find By Id").place(x=250, y=20)
        self.find_entry = Entry(win, textvariable=self.find_by_id)
        self.find_entry.place(x=310, y=20)
        # Find_By_National_Id
        self.find_by_national_id = StringVar()
        Label(win, text="Find By National Id").place(x=460, y=20)
        self.find_entry2 = Entry(win, textvariable=self.find_by_national_id)
        self.find_entry2.place(x=580, y=20)

        Button(win, text="New", width=7, command=self.reset_click).place(x=20, y=265)
        Button(win, text="Save", width=7, command=self.save_click).place(x=20, y=230)
        Button(win, text="Edit", width=7, command=self.edit_click).place(x=100, y=230)
        Button(win, text="Remove", width=7, command=self.remove_click).place(x=180, y=230)

        self.table = ttk.Treeview(win,
                                  column=(1, 2, 3, 4, 5, 6),
                                  show='headings'
                                  )
        self.table.bind("<<TreeviewSelect>>", self.select_product)
        self.show_on_table()

        self.table.heading(1, text="User ID")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="National Id")
        self.table.heading(5, text="Phone Num")
        self.table.heading(6, text="Car Id")
        # ---------------------------------------------

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=80)
        # -----------------------------------------------------
        self.table.bind("<<TreeviewSelect>>", self.select_product)
        self.find_entry.bind("<KeyRelease>", self.search_by_id)
        self.find_entry2.bind("<KeyRelease>", self.search_by_national_id)
        self.table.place(x=250, y=60)
        self.show_on_table()

        win.mainloop()


ui = UserView()
