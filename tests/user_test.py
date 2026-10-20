from model.user import User
from data_access.user_da import UserDA
from service.user_service import UserService

# =======================================================
# USER TEST --PASSED
# ========================================================
# user1=User(1,"ali","amiri","0441254698","09127455896")
#
# print(user1.to_tuple())
# print(user1.to_dict())


# =======================================
# Data Access Test
# =======================================
user_da = UserDA()

user1 = User(1, "ali", "amiri", "0441025986", "09127455896")
user2 = User(2, "reza", "moradi", "1234567890", "09191234567")

# user_da.save(user1)
# user_da.save(user2)

# print(user_da.find_all())
# print(user_da.find_by_id(1))
# print(user_da.find_by_national_id("0441254698"))
#
# user1.family = "amiri rad"
# user_da.update(user1)
# print(user_da.find_by_id(1))

# user_da.delete_by_id(2)
# print(user_da.find_all())


# =======================================
# Service Test PASSED
# =======================================
user_service = UserService()
User.phone_number="09126598321"
user_service.update(user1)
print(user_service.find_all())
# print("user save successfully..")
