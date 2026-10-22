from model.car import Car
from service.car_service import CarService
from utils.decorator import exception_handling


class CarController:

    @classmethod
    @exception_handling
    def save(cls, plate_number, model, year, color, vin_number, owner):
        car = Car(None, plate_number, model, year, color, vin_number, owner)
        CarService.save(car)
        return True, car

    @classmethod
    @exception_handling
    def update(cls, car_id, plate_number, model, year, color, vin_number, owner):
        car = Car(car_id, plate_number, model, year, color, vin_number, owner)
        CarService.update(car)
        return True, car

    @classmethod
    @exception_handling
    def delete(cls, car_id):
        delete_car=CarService.delete_by_id(car_id)
        return True, delete_car

    @classmethod
    @exception_handling
    def find_all(cls):
        cars = CarService.find_all()
        return True, cars

    @classmethod
    @exception_handling
    def find_by_id(cls, car_id):
        car = CarService.find_by_id(car_id)
        return True, car

    @classmethod
    @exception_handling
    def find_by_plate_number(cls, plate_number):
        car=CarService.find_by_plate(plate_number)
        return True, car

    @classmethod
    @exception_handling
    def find_by_vin(cls, vin):
        car=CarService.find_by_vin(vin)
        return True, car
