from utils.validation import *

class Service:
    def __init__(self,service_id,car_id,service_type,description,labor_cost,parts_cost,acceptance_date,acceptance_time):
        self.service_id = service_id
        self.car_id = car_id
        self.service_type = service_type
        self.description = description
        self.labor_cost = labor_cost
        self.parts_cost = parts_cost
        self.acceptance_date = acceptance_date
        self.acceptance_time = acceptance_time


    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        self._service_id = service_id

    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, car_id):
        self._car_id = car_id

    @property
    def service_type(self):
        return self._service_id

    @service_type.setter
    def service_type(self, service_type):
        self._service_type = Validation.service_type_validator(service_type)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = Validation.description_validator(description)


    @property
    def labor_cost(self):
        return self._labor_cost

    @labor_cost.setter
    def labor_cost(self,labor_cost):
        self._labor_cost = Validation.labor_cost_validator(labor_cost)

    @property
    def parts_cost(self):
        return self._parts_cost

    @parts_cost.setter
    def parts_cost(self, parts_cost):
        self._parts_cost = Validation.parts_cost_validator(parts_cost)

    @property
    def acceptance_date(self):
        return self._acceptance_date

    @acceptance_date.setter
    def acceptance_date(self, acceptance_date):
        self._acceptance_date = Validation.date_validator(acceptance_date,"error: invalid acceptance date!!!".title())

    @property
    def acceptance_time(self):
        return self._acceptance_time

    @acceptance_time.setter
    def acceptance_time(self, acceptance_time):
        self._acceptance_time = Validation.time_validator(acceptance_time,"error: invalid acceptance time!!!".title())






