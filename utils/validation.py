import re
from datetime import date


class ValidationError:
    @staticmethod
    def name_validator(name, message: str = "error:invalid name!!!".title()):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{3,30}$", name.strip()):
            return name.strip()
        else:
            raise ValueError(message)

    @staticmethod
    def family_validator(family, message: str = "error:invalid family!!!".title()):
        if isinstance(family, str) and re.match(r"^[a-zA-Z\s]{3,30}$", family.strip()):
            return family.strip()
        else:
            raise ValueError(message)

    @staticmethod
    def national_id_validator(national_id, message: str = "error:invalid national id!!!".title()):
        if isinstance(national_id, str) and re.match(r"^\d{3}\d{6}\d|\d{10}$", national_id):
            return national_id
        else:
            raise ValueError(message)

    @staticmethod
    def birth_validator(birth, message: str = "error:invalid birth!!!".title()):
        if isinstance(birth, date) and birth < date.today():
            return birth
        else:
            raise ValueError(message)

    @staticmethod
    def phone_number_validator(phone_number, message: str = "error:invalid phone number!!!".title()):
        if isinstance(phone_number, str) and re.match(r"^(09|\+989)\d{9}$", phone_number):
            return phone_number
        else:
            raise ValueError(message)

    @staticmethod
    def username_validator(username, message: str = "error:invalid username!!!".title()):
        if isinstance(username, str) and re.match(r"^[a-zA-Z0-9_]{3,30}$", username):
            return username
        else:
            raise ValueError(message)

    @staticmethod
    def password_validator(password, message: str = "error:invalid password!!!".title()):
        special_chars = r"!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?"
        if isinstance(password, str) and re.match(rf"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[{special_chars}]).{{8,30}}$",
                                                  password):
            return password
        else:
            raise ValueError(message)

    @staticmethod
    def role_validator(role, message: str = "error:invalid role!!!".title()):
        if isinstance(role, str) and re.match(r"^(admin|manager|operator)$", role):
            return role
        else:
            raise ValueError(message)

    @staticmethod
