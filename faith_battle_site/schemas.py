# from ninja import ModelSchema
from ninja import Schema

# from django.contrib.auth.models import User

class AuthUser(Schema):
    username: str
    password: str
    # class meta:
    #     model = User
    #     fields = ['username','password']

class NewUser(Schema):
    username: str
    password: str
    first_name: str
    avatar: int