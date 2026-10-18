import sqlite3


class UserDA:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect('repair_shop.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, user):
        self.connect()
        self.cursor.execute(
            """INSERT INTO USERS (name, family, national_id, phone_number)
               VALUES (?, ?, ?, ?)""",
            [user.name, user.family, user.national_id, user.phone_number]
        )
        self.disconnect(commit=True)

    def update(self, user):
        self.connect()
        self.cursor.execute(
            """UPDATE USERS
               SET name         = ?,
                   family       = ?,
                   national_id  = ?,
                   phone_number = ?
               WHERE user_id = ?""",
            [user.name, user.family, user.national_id, user.phone_number,user.user_id]
        )
        self.disconnect(commit=True)

    def delete_by_id(self, user_id):
        self.connect()
        self.cursor.execute("DELETE FROM USERS WHERE user_id = ?", [user_id])
        self.disconnect(commit=True)

    def find_by_id(self, user_id):
        self.connect()
        self.cursor.execute("SELECT * FROM USERS WHERE user_id = ?", [user_id])
        user = self.cursor.fetchone()
        self.disconnect()
        return user

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM USERS")
        user_list = self.cursor.fetchall()
        self.disconnect()
        return user_list
