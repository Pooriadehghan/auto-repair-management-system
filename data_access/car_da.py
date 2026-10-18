import sqlite3
from model.car import Car
from view.car_view import owner_national_id


class CarDA:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect('repair_shop.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""PRAGMA foreign_keys=ON;""")

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, car):
        self.connect()
        self.cursor.execute(
            """INSERT INTO CARS (national_id, plate_number, model, year, color, vin_number)
               VALUES (?, ?, ?, ?, ?, ?)""",
            [car.owner, car.plate_number, car.model, car.year, car.color, car.vin_number]
        )
        self.disconnect(commit=True)

    def update(self, car):
        self.connect()
        self.cursor.execute(
            """UPDATE CARS
               SET national_id  = ?,
                   plate_number = ?,
                   model        = ?,
                   year         = ?,
                   color        = ?,
                   vin_number   = ?
               WHERE car_id = ?""",
            [car.owner, car.plate_number, car.model, car.year, car.color, car.vin_number, car.car_id]
        )
        self.disconnect(commit=True)

    def delete_by_id(self, car_id):
        self.connect()
        self.cursor.execute("DELETE FROM CARS WHERE car_id = ?", [car_id])
        self.disconnect(commit=True)

    def find_by_id(self, car_id):
        self.connect()
        self.cursor.execute("SELECT * FROM CARS WHERE car_id = ?", [car_id])
        car = self.cursor.fetchone()
        self.disconnect()
        return car

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM CARS")
        car_list = self.cursor.fetchall()
        self.disconnect()
        return car_list

    def find_by_national_id(self, national_id):
        self.connect()
        self.cursor.execute("SELECT * FROM CARS WHERE national_id = ?", [national_id])
        car_list = self.cursor.fetchall()
        self.disconnect()
        return car_list

    # todo:از استاد پرسیده شود که در این بخش جستجو با کد ملی به جای پلاک مورد ثبول است یا خیر
