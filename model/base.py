class BaseModel:

    def to_dict(self):
        return {key.lstrip('_'): value for key, value in self.__dict__.items()}

    def to_tuple(self):
        return tuple(self.__dict__.values())
