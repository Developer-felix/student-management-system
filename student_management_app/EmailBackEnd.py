# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
# class EmailbackEnd(ModelBackend):
#     def authenticate(self,username=None,password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.all(email=username)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackEnd(ModelBackend):
    # def authenticate(self,request, username=None, password=None, **kwargs): solved this error by removing the self as bellow
    def authenticate(request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
