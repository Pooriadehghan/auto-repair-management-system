from model.base import BaseModel
from utils.validation import *


class Car(BaseModel):
    def __init__(self, car_id, plate_number, model, year, color, vin_number, owner):
        self.car_id = car_id
        self.plate_number = plate_number
        self.model = model
        self.year = year
        self.color = color
        self.vin_number = vin_number
        self.owner = owner

    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, car_id):
        self._car_id = car_id

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

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner
