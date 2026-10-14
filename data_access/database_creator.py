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
                       phone_number TEXT NOT NULL UNIQUE,
                       locked       TINYINT DEFAULT 0
                   );

                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS CARS
                   (
                       car_id       INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id      INTEGER NOT NULL REFERENCES USERS (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
                       plate_number TEXT    NOT NULL UNIQUE,
                       model        TEXT    NOT NULL,
                       year         INTEGER NOT NULL,
                       color        TEXT    NOT NULL,
                       vin_number   TEXT    NOT NULL UNIQUE,
                       locked       TINYINT DEFAULT 0

                   );


                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS SERVICES
                   (
                       service_id      INTEGER PRIMARY KEY AUTOINCREMENT,
                       car_id          INTEGER NOT NULL,
                       service_type    TEXT    NOT NULL,
                       description     TEXT,
                       labor_cost      REAL    NOT NULL DEFAULT 0,
                       parts_cost      REAL    NOT NULL DEFAULT 0,
                       acceptance_date TEXT    NOT NULL,
                       acceptance_time TEXT    NOT NULL,
                       locked          INTEGER          DEFAULT 0,

                       FOREIGN KEY (car_id) REFERENCES CARS (car_id)
                           ON UPDATE CASCADE
                           ON DELETE CASCADE
                   );
                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS INVOICES
                   (
                       invoice_id      INTEGER PRIMARY KEY AUTOINCREMENT,
                       car_id          INTEGER NOT NULL,
                       total_amount    REAL    NOT NULL,
                       discount_amount REAL    NOT NULL DEFAULT 0,
                       final_amount    REAL    NOT NULL,
                       payment_method  TEXT    NOT NULL,
                       status          TEXT    NOT NULL DEFAULT 'in_progress',
                       exit_date       TEXT,
                       exit_time       TEXT,
                       locked          INTEGER          DEFAULT 0,

                       FOREIGN KEY (car_id) REFERENCES CARS (car_id)
                           ON UPDATE CASCADE
                           ON DELETE CASCADE
                   );
                   """)

    connection.commit()
    cursor.close()
    connection.close()


create_connection()
print("Database created!")
