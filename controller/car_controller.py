from model.car import Car
from service.car_service import CarService
from utils.decorator import exception_handling


class CarController:
    car = CarService()

    @classmethod
    @exception_handling
    def save(cls, car_id,plate_number, model, year, color, vin_number, owner):
        car = Car(None, plate_number, model, year, color, vin_number, owner)
        cls.car.save(car)
        return True, car

    @classmethod
    @exception_handling
    def update(cls, car_id, plate_number, model, year, color, vin_number, owner):
        car = Car(car_id, plate_number, model, year, color, vin_number, owner)
        cls.car.update(car)
        return True, car

    @classmethod
    @exception_handling
    def delete(cls, car_id):
        delete_car = cls.car.delete_by_id(car_id)
        return True, delete_car

    @classmethod
    @exception_handling
    def find_all(cls):
        cars = CarService.find_all()
        return True, cars

    @classmethod
    @exception_handling
    def find_by_id(cls, car_id):
        car = cls.car.find_by_id(car_id)
        return True, car

    @classmethod
    @exception_handling
    def find_by_plate_number(cls, plate_number):
        car = cls.car.find_by_plate(plate_number)
        return True, car

    @classmethod
    @exception_handling
    def find_by_vin(cls, vin_number):
        car = cls.car.find_by_vin(vin_number)
        return True, car

    @classmethod
    @exception_handling
    def find_all(cls):
        cars = cls.car.find_all()
        return True, cars
