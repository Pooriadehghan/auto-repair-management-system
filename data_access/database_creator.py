import sqlite3


def create_connection():
    connection = sqlite3.connect('repair_shop.db')
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS USERS
                   (
                       user_id      INTEGER PRIMARY KEY AUTOINCREMENT,
                       name         TEXT NOT NULL,
                       family       TEXT NOT NULL,
                       national_id  TEXT NOT NULL UNIQUE,
                       phone_number TEXT NOT NULL
                   )
                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS CARS
                   (
                       car_id       INTEGER PRIMARY KEY AUTOINCREMENT,
                       national_id      INTEGER NOT NULL,
                       plate_number TEXT    NOT NULL UNIQUE,
                       model        TEXT    NOT NULL,
                       year         INTEGER NOT NULL,
                       color        TEXT    NOT NULL,
                       vin_number   TEXT    NOT NULL UNIQUE,

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
                   CREATE TABLE IF NOT EXISTS invoices
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
                           CHECK (status IN ('in_progress', 'completed', 'exited')),
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
