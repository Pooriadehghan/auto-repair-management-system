from model.base import BaseModel
from utils.validation import *


class User(BaseModel):
    def __init__(self, user_id, name, family, national_id, phone_number, car=None):
        self.user_id = user_id
        self.name = name
        self.family = family
        self.national_id = national_id
        self.phone_number = phone_number
        self.car = car

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validation.name_validator(name)

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validation.family_validator(family)

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        self._national_id = Validation.national_id_validator(national_id)

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = Validation.phone_number_validator(phone_number)

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, car):
        self._car = car
