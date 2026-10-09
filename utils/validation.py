import re
from datetime import date


from persian_tools import plate


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
    def plate_number_validator(plate_number, message: str = "error:invalid plate number!!!".title()):
        if isinstance(plate_number, str) and plate.is_valid(plate_number.strip()):
            return plate_number.strip()
        else:
            raise ValueError(message)

    @staticmethod
    def model_validator(model, message: str = "error:invalid model!!!".title()):
        if isinstance(model, str) and re.match(r"^[a-zA-Z0-9_\s\-]{3,30}$", model):
            return model.strip()
        else:
            raise ValueError(message)

    @staticmethod
    def year_validator(year, message: str = "error:invalid year!!!".title()):
        if isinstance(year, int) and 2000 < year < 2026:
            return year
        else:
            raise ValueError(message)

    @staticmethod
    def color_validator(color, message: str = "error:invalid color!!!".title()):
        if isinstance(color, str) and re.match(r"^[a-zA-Z]{3,15}$", color):
            return color.strip()
        else:
            raise ValueError(message)

    @staticmethod
    def vin_number_validator(vin_number, message: str = "error:invalid vin number!!!".title()):
        if isinstance(vin_number, str) and re.match(r"^[A-HJ-NPR-Z0-9]{17}$", vin_number.strip().upper()):
            return vin_number.strip().upper()
        else:
            raise ValueError(message)

    @staticmethod
    def kilometer_validator(kilometer, message: str = "error:invalid kilometer!!!".title()):
        if isinstance(kilometer, int) and 0 < kilometer < 200000:
            return kilometer
        else:
            raise ValueError(message)

    @staticmethod
    def service_type_validator(service_type, message: str = "error:invalid service_type!!!".title()):
        if isinstance(service_type, str) and re.match(
                r"^(repairs|periodic_service|pdr|car_wash|carwash|periodicservice)$",
                service_type.strip().lower()):
            return service_type.strip().lower()
        else:
            raise ValueError(message)

    @staticmethod
    def description_validator(description, message: str = "error:invalid description!!!".title()):
        if isinstance(description, str) and description.strip() != "" and 3 < len(description.strip()) < 200:
            return description.strip()
        else:
            raise ValueError(message)

    @staticmethod
    def labor_cost_validator(labor_cost, message: str = "error:invalid labor cost!!!".title()):
        if isinstance(labor_cost, float) and 0 <= labor_cost:
            return labor_cost
        else:
            raise ValueError(message)

    @staticmethod
    def parts_used_validator(parts_used, message: str = "error:invalid parts used!!!".title()):
        if isinstance(parts_used, str) and parts_used.strip() != "":
            return parts_used.strip()
        else:
            raise ValueError(message)

    @staticmethod
    def parts_label_validator(parts_label, message: str = "error:invalid parts label!!!".title()):
        if isinstance(parts_label, str) and re.match(r"^[a-zA-Z0-9]{3,50}$", parts_label.strip().lower()):
            return parts_label.strip().lower()
        else:
            raise ValueError(message)

    @staticmethod
    def parts_cost_validator(parts_cost, message: str = "error:invalid parts cost!!!".title()):
        if isinstance(parts_cost, (int, float)) and 0 < parts_cost:
            return parts_cost
        else:
            raise ValueError(message)

    @staticmethod
    def mechanic_name_validator(mechanic_name, message: str = "error:invalid mechanic name!!!".title()):
        if isinstance(mechanic_name, str) and re.match(r"^[a-zA-Z\s]{3,50}$", mechanic_name.strip()):
            return mechanic_name.strip()
        else:
            raise ValueError(message)

    @staticmethod
    def item_replace_validator(item_replace, message: str = "error:invalid item replace!!!".title()):
        if isinstance(item_replace, str) and item_replace.strip() != "" and re.match(r"^[a-zA-Z0-9\s]{3,50}$",
                                                                                     item_replace.strip().lower()):
            return item_replace.strip()
        else:
            raise ValueError(message)

    @staticmethod
    def item_cost_validator(item_cost, message: str = "error:invalid parts cost!!!".title()):
        if isinstance(item_cost, (int, float)) and 0 < item_cost:
            return item_cost
        else:
            raise ValueError(message)

    @staticmethod
    def service_interval_validator(service_interval, message: str = "error:invalid service_interval!!!".title()):
        if isinstance(service_interval, int) and 1_000 < service_interval < 10_000:
            return service_interval
        else:
            raise ValueError(message)

    @staticmethod
    def next_service_mileage_validator(
            next_service_mileage,
            current_km,
            message: str = "error:invalid next_service_mileage!!!".title()
    ):
        if (isinstance(next_service_mileage, int)
                and isinstance(current_km, int)
                and 0 <= current_km < next_service_mileage):
            return next_service_mileage
        else:
            raise ValueError(message)

    @staticmethod
    def body_part_validator(body_part, message: str = "error:invalid body_part!!!".title()):
        if isinstance(body_part, str) and body_part.strip() != "" and re.match(r"^[a-zA-Z0-9\s]{3,50}$",
                                                                               body_part.strip().lower()):
            return body_part.strip().lower()
        else:
            raise ValueError(message)

    @staticmethod
    def damage_service_validator(damage_service, message: str = "error:invalid damage_service!!!".title()):
        if isinstance(damage_service, str) and damage_service.strip() != "" and re.match(r"^[a-zA-Z0-9\s]{3,50}$",
                                                                                         damage_service.strip().lower()):
            return damage_service.strip().lower()
        else:
            raise ValueError(message)

    @staticmethod
    def material_cost_validator(material_cost, message: str = "error:invalid material cost!!!".title()):
        if isinstance(material_cost, (int, float)) and 0 < material_cost:
            return material_cost
        else:
            raise ValueError(message)

    @staticmethod
    def technician_name_validator(technician_name, message: str = "error:invalid technician name!!!".title()):
        if isinstance(technician_name, str) and re.match(r"^[a-zA-Z\s]{3,50}$", technician_name.strip()):
            return technician_name.strip()
        else:
            raise ValueError(message)

    @staticmethod
    def wash_type_validator(wash_type, message: str = "error:invalid wash type!!!".title()):
        if isinstance(wash_type, str) and re.match(r"^(normal|full|interior|exterior)$", wash_type.strip().lower()):
            return wash_type.strip().lower()
        else:
            raise ValueError(message)

    @staticmethod
    def consumable_cost_validator(consumable_cost, message: str = "error:invalid consumable cost!!!".title()):
        if isinstance(consumable_cost, (int, float)) and 0 < consumable_cost:
            return consumable_cost
        else:
            raise ValueError(message)

    @staticmethod
    def total_service_cost_validator(total_service_cost, message: str = "error:invalid total service cost!!!".title()):
        if isinstance(total_service_cost, (int, float)) and 0 < total_service_cost < 1_000_000_000:
            return total_service_cost
        else:
            raise ValueError(message)

    @staticmethod
    def discount_validator(discount, total_service_cost, message: str = "error:invalid discount!!!".title()):
        if isinstance(discount, (int, float) and
                                isinstance(total_service_cost, (int, float)) and
                                0 <= discount <= total_service_cost):
            return discount
        else:
            raise ValueError(message)

    @staticmethod
    def final_amount_validator(final_amount, total_service_cost, discount,
                               message: str = "error:invalid final amount!!!".title()):
        if isinstance(final_amount, (int, float) and
                                    isinstance(total_service_cost, (int, float)) and
                                    isinstance(discount, (int, float)) and
                                    final_amount >= 0 and
                                    final_amount == total_service_cost + discount):
            return final_amount
        else:
            raise ValueError(message)

    @staticmethod
    def payment_method_validator(payment_method, message: str = "error:invalid payment method!!!".title()):
        if isinstance(payment_method, str) and payment_method.strip() != "" and re.match(r"^(cash|card|pos|transfer)$",
                                                                                         payment_method.strip().lower()):
            return payment_method.strip().lower()
        else:
            raise ValueError(message)

    @staticmethod
    def receiver_name_validator(receiver_name, message: str = "error:invalid receiver name!!!".title()):
        if isinstance(receiver_name, str) and re.match(r"^[a-zA-Z\s]{3,30}$", receiver_name.strip()):
            return receiver_name.strip()
        else:
            raise ValueError(message)

