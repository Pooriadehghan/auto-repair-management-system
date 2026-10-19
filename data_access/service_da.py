import os
import sqlite3


class ServiceDA:
    def __init__(self):
        self.connection = None
        self.cursor = None

    # def connect(self):
    #     self.connection = sqlite3.connect("repair_shop.db")
    #     self.cursor = self.connection.cursor()
    #     self.cursor.execute("PRAGMA foreign_keys = ON")

    def connect(self):
        base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
        db_path = os.path.join(base_dir, "repair_shop.db")

        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()

        self.cursor.close()
        self.connection.close()

    def save(self, service):
        self.connect()
        self.cursor.execute(
            """INSERT INTO SERVICES (service_type, description, labor_cost)
               VALUES (?, ?, ?)""",
            [service.service_type, service.description, service.labor_cost]
        )
        self.disconnect(commit=True)

    def update(self, service):
        self.connect()
        self.cursor.execute(
            """UPDATE SERVICES
               SET service_type = ?,
                   description  = ?,
                   labor_cost   = ?
               WHERE service_id = ?""",
            [
                service.service_type,
                service.description,
                service.labor_cost,
                service.service_id
            ]
        )
        self.disconnect(commit=True)

    def delete_by_id(self, service_id):
        self.connect()
        self.cursor.execute(
            "DELETE FROM SERVICES WHERE service_id = ?",
            [service_id]
        )
        self.disconnect(commit=True)

    def find_by_id(self, service_id):
        self.connect()
        self.cursor.execute(
            "SELECT * FROM SERVICES WHERE service_id = ?",
            [service_id]
        )
        service = self.cursor.fetchone()
        self.disconnect()
        return service

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM SERVICES")
        service_list = self.cursor.fetchall()
        self.disconnect()
        return service_list
