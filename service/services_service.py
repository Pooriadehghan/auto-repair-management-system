from data_access.service_da import ServiceDA

class ServiceService:
    def __init__(self):
        self.da = ServiceDA()


    def save(self, service):
        if self.da.find_by_id(service.service_id):
            raise ValueError("service already exists!!!")
        self.da.save(service)


    def update(self,service):
        if not self.da.find_by_id(service.service_id):
            raise ValueError("service not found!!!")
        self.da.update(service)

    def delete_by_id(self, service_id):
        if not self.da.find_by_id(service_id):
            raise ValueError("service not found!!!")
        self.da.delete_by_id(service_id)

    def find_by_id(self, service_id):
        return self.da.find_by_id(service_id)

    def find_all(self):
        return self.da.find_all()

