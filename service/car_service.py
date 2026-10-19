from data_access.car_da import CarDA


class CarService:
    def __init__(self):
        self.da = CarDA()

    def save(self, car):
        if self.da.find_by_plate(car.plate_number):
            raise ValueError("ERROR:plate number already exists!!!")
        if self.da.find_by_vin(car.vin):
            raise ValueError("ERROR:vin number already exists!!!")

        # todo:بررسی با کدملی مالک نیاز دارد؟
        self.da.save(car)

    def update(self, car):
        if not self.da.find_by_id(car.id):
            raise ValueError("ERROR:Car Not Found!!!")

        # todo:برای تکمیل این بخش از استاد سوال شود
        self.da.update(car)

    def delete_by_id(self, car_id):
        self.da.delete_by_id(car_id)

    def find_by_id(self, car_id):
        return self.da.find_by_id(car_id)

    def find_all(self):
        return self.da.find_all()

    def find_by_plate(self, plate_number):
        return self.da.find_by_plate(plate_number)

    def find_by_vin(self, vin):
        return self.da.find_by_vin(vin)
