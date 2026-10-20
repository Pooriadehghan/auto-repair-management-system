from model.base import BaseModel
from utils.validation import *


class Service(BaseModel):
    def __init__(self, service_id, service_type, description, labor_cost):
        self.service_id = service_id
        self.service_type = service_type
        self.description = description
        self.labor_cost = labor_cost

    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        self._service_id = service_id


    @property
    def service_type(self):
        return self._service_type

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
    def labor_cost(self, labor_cost):
        self._labor_cost = Validation.labor_cost_validator(labor_cost)

    #
    # @property
    # def total_cost(self):
    #     return self.labor_cost + self.parts_cost
