from model.user import User
from service.user_service import UserService
from utils.decorator import exception_handling


class UserController:
    service = UserService()

    @classmethod
    @exception_handling
    def save(cls, user_id, name, family, national_id, phone_number):
        user = User(None, name, family, national_id, phone_number)
        cls.service.save(user)
        return True, user

    @classmethod
    @exception_handling
    def update(cls, user_id, name, family, national_id, phone_number):
        user = User(user_id, name, family, national_id, phone_number)
        cls.service.update(user)
        return True, user

    @classmethod
    @exception_handling
    def delete(cls, user_id):
        delete_user = cls.service.delete_by_id(user_id)
        return True, delete_user

    @classmethod
    @exception_handling
    def find_all(cls):
        users = cls.service.find_all()
        return True, users

    @classmethod
    @exception_handling
    def find_by_id(cls, user_id):
        find_user = cls.service.find_by_id(user_id)
        return True, find_user

    @classmethod
    @exception_handling
    def find_by_national_id(cls, national_id):
        find_user = cls.service.find_by_national_id(national_id)
        return True, find_user
