import os
import sqlite3
from model.car import Car


class CarDA:
    def __init__(self):
        self.connection = None
        self.cursor = None

    # def connect(self):
    #     self.connection = sqlite3.connect('repair_shop.db')
    #     self.cursor = self.connection.cursor()
    #     self.cursor.execute("""PRAGMA foreign_keys=ON;""")

    def connect(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "repair_shop.db")

        # print(">>> Connecting to Database Path:", db_path)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, car):
        self.connect()
        national_id = car.owner.national_id if hasattr(car.owner, 'national_id') else car.owner
        # print("DEBUG - extracted national_id:", national_id)
        self.cursor.execute(
            """INSERT INTO CARS (plate_number,model,year,color,vin_number,national_id)
               VALUES (?, ?, ?, ?, ?, ?)""",
            [car.plate_number,car.model,car.year,car.color,car.vin_number,national_id]
        )
        self.disconnect(commit=True)

    def update(self, car):
        self.connect()
        national_id = car.owner.national_id if hasattr(car.owner, 'national_id') else car.owner
        self.cursor.execute(
            """UPDATE CARS
               SET plate_number = ?,
                   model        = ?,
                   year         = ?,
                   color        = ?,
                   vin_number   = ?,
                   national_id  = ?
               WHERE car_id = ?""",
            [car.plate_number, car.model, car.year, car.color, car.vin_number, national_id, car.car_id]
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

    def find_by_plate(self, plate_number):
        self.connect()
        self.cursor.execute(
            "SELECT * FROM CARS WHERE plate_number = ?",
            [plate_number]
        )
        result = self.cursor.fetchone()
        self.disconnect()
        return result

    def find_by_vin(self, vin_number):
        self.connect()
        try:
            self.cursor.execute(
                "SELECT * FROM CARS WHERE vin_number = ?",
                [vin_number]
            )
            return self.cursor.fetchone()
        finally:
            self.disconnect()
