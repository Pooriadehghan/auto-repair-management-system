from model.base import BaseModel
from utils.validation import *


class Invoice(BaseModel):
    def __init__(self, invoice_id, car_id, parts_cost=0, total_service_cost=0, discount_amount=0
                 , payment_method="transfer", date_exit=None, time_exit=None, status="in_progress",
                 acceptance_timestamp=None):
        self.invoice_id = invoice_id
        self.car_id = car_id
        self.parts_cost = parts_cost
        self.total_service_cost = total_service_cost
        self.discount_amount = discount_amount
        self.payment_method = payment_method
        self.date_exit = date_exit
        self.time_exit = time_exit
        self.status = status
        self.acceptance_timestamp = acceptance_timestamp

    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        self._invoice_id = invoice_id

    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, car_id):
        self._car_id = car_id

    @property
    def parts_cost(self):
        return self._parts_cost

    @parts_cost.setter
    def parts_cost(self, parts_cost):
        self._parts_cost = Validation.parts_cost_validator(parts_cost)

    @property
    def total_service_cost(self):
        return self._total_service_cost

    @total_service_cost.setter
    def total_service_cost(self, total_service_cost):
        self._total_service_cost = Validation.total_service_cost_validator(total_service_cost)

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        self._discount_amount = Validation.discount_validator(discount_amount, self.total_service_cost, self.parts_cost)

    # --------------------------------------------
    @property
    # todo:از استاد پرسیده شود
    def final_amount(self):
        return (self._total_service_cost + self._parts_cost) - self._discount_amount

    # -----------------------------------------------
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        self._payment_method = Validation.payment_method_validator(payment_method)

    @property
    def date_exit(self):
        return self._date_exit

    @date_exit.setter
    def date_exit(self, date_exit):
        if date_exit is None or date_exit == "":
            self._date_exit = None
        else:
            self._date_exit = Validation.date_validator(date_exit)

    @property
    def time_exit(self):
        return self._time_exit

    @time_exit.setter
    def time_exit(self, time_exit):
        if time_exit is None or time_exit == "":
            self._time_exit = None
        else:
            self._time_exit = Validation.time_validator(time_exit)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = Validation.status_validator(status)

    @property
    def acceptance_timestamp(self):
        return self._acceptance_timestamp

    @acceptance_timestamp.setter
    def acceptance_timestamp(self, acceptance_timestamp):
        if acceptance_timestamp is None or acceptance_timestamp == "":
            self._acceptance_timestamp = None
        else:
            self._acceptance_timestamp = str(acceptance_timestamp)
