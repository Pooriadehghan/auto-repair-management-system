
from utils.validation import *


class User:
    def __init__(self,user_id,name,family,national_id,phone_number,username,password,role):
        self.user_id = user_id
        self.name = name
        self.family = family
        self.national_id = national_id
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.role = role


    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id =user_id


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name =Validation.name_validator(name)

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family =Validation.family_validator(family)

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        self._national_id =Validation.national_id_validator(national_id)

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number =Validation.phone_number_validator(phone_number)


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username =Validation.username_validator(username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password =Validation.password_validator(password)

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role =Validation.role_validator(value)