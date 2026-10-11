from utils.validation import *

class Invoice:
    def __init__(self,invoice_id,car_id,total_service_cost,discount_amount,
                 final_amount,payment_method,date_exit,time_exit):
        self.invoice_id = invoice_id
        self.car_id = car_id
        self.total_service_cost = total_service_cost
        self.discount_amount = discount_amount
        self.final_amount = final_amount
        self.payment_method = payment_method
        self.date_exit = date_exit
        self.time_exit = time_exit


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
    def total_service_cost(self):
        return self.total_service_cost

    @total_service_cost.setter
    def total_service_cost(self, total_service_cost):
        self.total_service_cost = Validation.total_service_cost_validator(total_service_cost)

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        self._discount_amount = Validation.discount_validator(discount_amount)

    @property
    def final_amount(self):
        return self._final_amount

    @final_amount.setter
    def final_amount(self, final_amount):
        self._final_amount = Validation.final_amount_validator(final_amount)

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
        self._date_exit=Validation.date_validator(date_exit)

    @property
    def time_exit(self):
        return self._time_exit

    @time_exit.setter
    def time_exit(self,time_exit):
        self._time_exit=Validation.time_validator(time_exit)