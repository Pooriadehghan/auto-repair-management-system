class BaseModel:

    def to_dict(self):
        return self.__dict__

    def to_tuple(self):
        return tuple(self.__dict__.values())
