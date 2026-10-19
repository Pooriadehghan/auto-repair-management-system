from data_access.car_da import CarDA
from model.car import Car


# ==================================================
# CAR TEST ---PASSED
# ==================================================
#
# car1 = Car(5,"amir","amiri","+989358966554","44m123iran40",
#            "benz e200",2016,"black","EWE12365478965475")
#
#
# print(car1.to_tuple())
# print(car1.to_dict())
# ==================================================
# DATA ACCESS TEST ---PASSED
# ==================================================
car_da = CarDA()

car1=Car(1,"12m123iran44","benz c200",2016,"black","EWE12365478965475")
car1=Car(2,"12m123iran40","bmw 730li",2024,"white","EWE12365478966587")

car_da.save(car1)

print(car_da.find_all())
