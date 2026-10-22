from data_access.user_da import UserDA


class UserService:
    def __init__(self):
        self.da = UserDA()

    def save(self, user):
        if self.da.find_by_national_id(user.national_id):
            raise ValueError("ERORR:National ID already exists!!!")
        if self.da.find_by_phone_number(user.phone_number):
            raise ValueError("ERORR:Phone number already exists!!!")

        self.da.save(user)

    def update(self, user):
        existing_user = self.da.find_by_id(user.user_id)
        if not existing_user:
            raise ValueError("ERORR:User does not exist for update")

        if not user.phone_number or len(user.phone_number) < 11:
            raise ValueError("ERROR: Invalid Phone Number")

        self.national_id_validator(user.national_id)
        national_id_user = self.da.find_by_national_id(user.national_id)
        if national_id_user and national_id_user[0] != user.user_id:
            raise ValueError("ERROR: National ID cannot be empty")

        return self.da.update(user)

    def delete_by_id(self, user_id):
        if not self.da.find_by_id(user_id):
            raise ValueError("ERORR:User does not exist for delete")
        self.da.delete_by_id(user_id)

    def find_by_id(self, user_id):
        return self.da.find_by_id(user_id)

    def find_by_national_id(self, national_id):
        return self.da.find_by_national_id(national_id)

    def find_by_phone_number(self, phone_number):
        return self.da.find_by_phone_number(phone_number)

    @classmethod
    def find_all(cls):
        da = UserDA()
        return da.find_all()
