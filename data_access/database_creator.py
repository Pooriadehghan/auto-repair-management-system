import sqlite3
import os


def create_connection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "repair_shop.db")
    print(f"Connecting to DB at: {db_path} | Exists: {os.path.exists(db_path)}")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS USERS
                   (
                       user_id      INTEGER PRIMARY KEY AUTOINCREMENT,
                       name         TEXT NOT NULL,
                       family       TEXT NOT NULL,
                       national_id  TEXT NOT NULL UNIQUE,
                       phone_number TEXT NOT NULL,
                       car_id       INTEGER UNIQUE,
                       FOREIGN KEY (car_id) REFERENCES CARS (car_id)
                   );
                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS CARS
                   (
                       car_id       INTEGER PRIMARY KEY AUTOINCREMENT,
                       plate_number TEXT    NOT NULL UNIQUE,
                       model        TEXT    NOT NULL,
                       year         INTEGER NOT NULL,
                       color        TEXT    NOT NULL,
                       vin_number   TEXT    NOT NULL UNIQUE,
                       national_id  TEXT    NOT NULL,

                       FOREIGN KEY (national_id)
                           REFERENCES USERS (national_id)
                           ON UPDATE CASCADE
                           ON DELETE RESTRICT
                   )
                   """)
    cursor.execute("DROP TABLE IF EXISTS SERVICES")

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS SERVICES
                   (
                       service_id   INTEGER PRIMARY KEY AUTOINCREMENT,
                       service_type TEXT NOT NULL,
                       description  TEXT,
                       labor_cost   REAL NOT NULL DEFAULT 0
                   )
                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS INVOICES
                   (
                       invoice_id           INTEGER PRIMARY KEY AUTOINCREMENT,
                       car_id               INTEGER NOT NULL,
                       parts_cost           REAL    NOT NULL DEFAULT 0,
                       total_service_cost   REAL    NOT NULL DEFAULT 0,
                       discount_amount      REAL    NOT NULL DEFAULT 0,

                       final_amount         REAL GENERATED ALWAYS AS (
                           parts_cost + total_service_cost - discount_amount
                           ) STORED,

                       payment_method       TEXT    NOT NULL DEFAULT 'transfer',
                       date_exit            TEXT,
                       time_exit            TEXT,
                       status               TEXT    NOT NULL DEFAULT 'in_progress'
                           CHECK (status IN ('in progress', 'completed', 'exited')),
                       acceptance_timestamp TEXT,

                       FOREIGN KEY (car_id)
                           REFERENCES CARS (car_id)
                           ON UPDATE CASCADE
                           ON DELETE RESTRICT
                   )
                   """)

    connection.commit()
    cursor.close()
    connection.close()


create_connection()
print("Database created!")
