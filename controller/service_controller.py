from model.service import Service
from service.services_service import ServiceService
from utils.decorator import exception_handling


class ServiceController:

    @classmethod
    @exception_handling
    def save(cls, service_type, description, labor_cost):
        service = Service(None, service_type, description, labor_cost)
        ServiceService.save(service)
        return True, service

    @classmethod
    @exception_handling
    def update(cls, service_id, service_type, description, labor_cost):
        service = Service(service_id, service_type, description, labor_cost)
        ServiceService.update(service)
        return True, service

    @classmethod
    @exception_handling
    def delete(cls, service_id):
        delete_service = ServiceService.delete_by_id(service_id)
        return True, delete_service

    @classmethod
    @exception_handling
    def find_by_id(cls, service_id):
        find_service = ServiceService.find_by_id(service_id)
        return True, find_service

    @classmethod
    @exception_handling
    def find_all(cls):
        find_service = ServiceService.find_all()
        return True, find_service
