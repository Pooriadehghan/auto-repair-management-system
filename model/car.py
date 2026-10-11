from utils.validation import *


class Car:
    def __init__(self, car_id, name_customer, family_customer, phone_number, plate_number,
                 model, year, color, vin_number):
        self._car_id = car_id
        self._name_customer = name_customer
        self._family_customer = family_customer
        self._phone_number = phone_number
        self._plate_number = plate_number
        self._model = model
        self._year = year
        self._color = color
        self._vin_number = vin_number

    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, car_id):
        self._car_id = car_id

    @property
    def name_customer(self):
        return self._name_customer

    @name_customer.setter
    def name_customer(self, name_customer):
        self._name_customer = Validation.name_validator(name_customer, "Error:invalid name customer".title())

    @property
    def family_customer(self):
        return self._family_customer

    @family_customer.setter
    def family_customer(self, family_customer):
        self._family_customer = Validation.family_validator(family_customer, "Error:invalid family customer".title())

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = Validation.phone_number_validator(phone_number,
                                                               "Error:invalid customer phone number".title())

    @property
    def plate_number(self):
        return self._plate_number

    @plate_number.setter
    def plate_number(self, plate_number):
        self._plate_number = Validation.plate_number_validator(plate_number)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = Validation.model_validator(model)

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = Validation.year_validator(year)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = Validation.color_validator(color)

    @property
    def vin_number(self):
        return self._vin_number

    @vin_number.setter
    def vin_number(self, vin_number):
        self._vin_number = Validation.vin_number_validator(vin_number)
