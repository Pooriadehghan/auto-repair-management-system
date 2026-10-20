
from model.service import Service
from data_access.service_da import ServiceDA


# ======================================================================
# SERVICE TEST----PASSED
# ======================================================================

service1 = Service(1,"carwash","just wash out",250.0)
service2 = Service(2,"pdr","pdr dar samt rast aghab",2010.0)


# print(service1.to_dict())
# print(service1.to_tuple())

# ======================================================================
#DATA ACCESS TEST ----------PASSED
# ======================================================================
service_da=ServiceDA()

# service_da.save(service1)
# service_da.save(service2)

# Service.labor_cost=260.0
# service_da.update(service1)

# service_da.delete_by_id(1)

# print(service_da.find_all())

# print("DONE")


# ======================================================================
# ----------PASSED
# ======================================================================




