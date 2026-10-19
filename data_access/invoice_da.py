import os
import sqlite3


class InvoiceDA:
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

    def save(self, invoice):
        self.connect()
        self.cursor.execute(
            """INSERT INTO INVOICES (car_id,
                                     parts_cost,
                                     total_service_cost,
                                     discount_amount,
                                     payment_method,
                                     date_exit,
                                     time_exit,
                                     status,
                                     acceptance_timestamp)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                invoice.car_id,
                invoice.parts_cost,
                invoice.total_service_cost,
                invoice.discount_amount,
                invoice.payment_method,
                invoice.date_exit,
                invoice.time_exit,
                invoice.status,
                invoice.acceptance_timestamp
            )
        )
        self.disconnect(commit=True)

    def update(self, invoice):
        self.connect()
        self.cursor.execute(
            """UPDATE INVOICES
               SET car_id               = ?,
                   parts_cost           = ?,
                   total_service_cost   = ?,
                   discount_amount      = ?,
                   payment_method       = ?,
                   date_exit            = ?,
                   time_exit            = ?,
                   status               = ?,
                   acceptance_timestamp = ?
               WHERE invoice_id = ?""",
            (
                invoice.car_id,
                invoice.parts_cost,
                invoice.total_service_cost,
                invoice.discount_amount,
                invoice.payment_method,
                invoice.date_exit,
                invoice.time_exit,
                invoice.status,
                invoice.acceptance_timestamp,
                invoice.invoice_id
            )
        )
        self.disconnect(commit=True)

    def delete_by_id(self, invoice_id):
        self.connect()
        self.cursor.execute(
            "DELETE FROM INVOICES WHERE invoice_id = ?",
            (invoice_id,)
        )
        self.disconnect(commit=True)

    def find_by_id(self, invoice_id):
        self.connect()
        self.cursor.execute(
            "SELECT * FROM INVOICES WHERE invoice_id = ?",
            (invoice_id,)
        )
        invoice = self.cursor.fetchone()
        self.disconnect()
        return invoice

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM INVOICES")
        invoice_list = self.cursor.fetchall()
        self.disconnect()
        return invoice_list

    def find_by_car_id(self, car_id):
        self.connect()
        self.cursor.execute(
            "SELECT * FROM INVOICES WHERE car_id = ?",
            (car_id,)
        )
        invoice_list = self.cursor.fetchall()
        self.disconnect()
        return invoice_list

    def find_by_date_range(self, start_date, end_date):
        self.connect()
        self.cursor.execute(
            """
            SELECT *
            FROM INVOICES
            WHERE acceptance_timestamp BETWEEN ? AND ?
            """,
            (start_date, end_date),
        )
        rows = self.cursor.fetchall()
        self.disconnect()
        return rows
