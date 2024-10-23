from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponseBadRequest

from ninja import NinjaAPI

from .schemas import AuthUser, NewUser
# from player_site.models import Card
from .security import createAccessToken

from users.views import getAvatarFileList


api = NinjaAPI()


# @api.get("/")
# def stats(request):
#     active_cards = Card.objects.filter(is_active=True).order_by("slug")
#     active_cards_ = list(map(lambda x: x.slug, active_cards))
#     return {
#         'active_cards': active_cards_
#     }

@api.post("/user")
def createUser(request, new_user: NewUser):
    user = User.objects.filter(username=new_user.username).first()
    if user:
        return HttpResponseForbidden('username already in use')
    user = User.objects.create_user(username=new_user.username, password=new_user.password,first_name=new_user.first_name, last_name=new_user.avatar)

@api.get("/user/{user_id}")
def stats(request, user_id:int):
    user_data = User.objects.filter(id=user_id).values('id', 'last_login', 'username', 'email', 'last_name')[0]
    user_data["last_login"] = str(user_data["last_login"])
    if user_data["email"] != "":
        splited_email_adress = str(user_data["email"]).split('@')
        joined_email_adress = splited_email_adress[0][:3]+ '*'*(len(splited_email_adress[0])-3) + "@" + splited_email_adress[1]
        user_data["email"] = joined_email_adress
    return user_data

@api.get("/avatar_list")
def stats(request):

    return {'avatar_list':getAvatarFileList()}


@api.post("/auth")
def auth(request, user: AuthUser):
    _user = User.objects.filter(username=user.username).first()
    if _user is None:
        return HttpResponseBadRequest('username not founded')
    if _user.is_active == False:
        return HttpResponseForbidden('user deactivated')
    authenticated_user = authenticate(
        username=user.username, password=user.password)
    if authenticated_user:
        login(request, authenticated_user)
        access_token = createAccessToken({
            "sub": authenticated_user.id,
        })
        return {
            'id': authenticated_user.id,
            'access_token': access_token
        }
    return HttpResponseForbidden('username and password do not match')
