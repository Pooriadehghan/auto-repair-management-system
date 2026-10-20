from data_access.car_da import CarDA


class CarService:
    def __init__(self):
        self.da = CarDA()

    def save(self, car):
        if self.da.find_by_plate(car.plate_number):
            raise ValueError("ERROR:plate number already exists!!!")
        if self.da.find_by_vin(car.vin):
            raise ValueError("ERROR:vin number already exists!!!")

        if hasattr(car, 'owner') and car.owner:
            national_id = car.owner.national_id if hasattr(car.owner, 'national_id') else car.owner
            if not self.user_da.find_by_national_id(national_id):
                raise ValueError("ERROR: Car owner does not exist in database!")
        self.da.save(car)

    def update(self, car):
        if not self.da.find_by_id(car.id):
            raise ValueError("ERROR:Car Not Found!!!")
        duplicate_plate_car = self.da.find_by_plate(car.plate_number)
        if duplicate_plate_car is not None and duplicate_plate_car.id != car.id:
            raise ValueError("ERROR: Plate number already exists!")

        duplicate_vin_car = self.da.find_by_vin(car.vin)
        if duplicate_vin_car is not None and duplicate_vin_car.id != car.id:
            raise ValueError("ERROR: VIN number already exists!")

        if hasattr(car, 'owner') and car.owner:
            national_id = car.owner.national_id if hasattr(car.owner, 'national_id') else car.owner
            if not self.user_da.find_by_national_id(national_id):
                raise ValueError("ERROR: Car owner does not exist in database!")
        self.da.update(car)

    def delete_by_id(self, car_id):
        if not self.da.find_by_id(car_id):
            raise ValueError("ERROR: Car not found!")
        self.da.delete_by_id(car_id)

    def find_by_id(self, car_id):
        return self.da.find_by_id(car_id)

    def find_all(self):
        return self.da.find_all()

    def find_by_plate(self, plate_number):
        return self.da.find_by_plate(plate_number)

    def find_by_vin(self, vin):
        return self.da.find_by_vin(vin)
