from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpRequest

from ninja import NinjaAPI

from .schemas import AuthUser, NewUser
# from player_site.models import Card
from .security import createAccessToken

from users.models import Jogador
from games.models import Game, GameBoard, CardFamily, Card
from utils.files import getAvatarFileList, gerarArquivo


api = NinjaAPI()


@api.get("/")
def stats(request):
    # TODO: retornar dados do servidor em geral, como versão, etc.
    # active_cards = Card.objects.filter(is_active=True).order_by("slug")
    # active_cards_ = list(map(lambda x: x.slug, active_cards))
    return {
        # 'active_cards': active_cards_,
        'avatar_list': getAvatarFileList(),
    }


@api.get("/avatar_list")
def avatarList(request: HttpRequest):
    return {'avatar_list': getAvatarFileList(show_all=request.user.is_staff)}


@api.get("/games")
def games(request):
    # active_cards = Card.objects.filter(is_active=True).order_by("slug")
    # active_cards_ = list(map(lambda x: x.slug, active_cards))
    all_games = Game.objects.all()
    return {game.id: game.title for game in all_games}


def getCardsbyFamily(card_family_id: int, is_DLC: bool = False):
    card_list = Card.objects.filter(card_family=card_family_id)
    if is_DLC:
        return [
            [f'/media/{card.card_image.name}',
             f'/media/{card.card_image_mini.name}']
            for card in card_list]
    return [{card.slug: {
        'card_description': card.card_description,
        'card_image': card.card_image.url,
        'card_image_mini': card.card_image_mini.url,
        'top_left_value': card.top_left_value,
        'top_right_value': card.top_right_value,
        'bottom_left_value': card.bottom_left_value,
        'bottom_right_value': card.bottom_right_value,
    }} for card in card_list]


@api.get("/games/{game_id}")
def gameDetails(request, game_id: int):
    game = Game.objects.get(id=game_id)
    gameBoard = GameBoard.objects.filter(game=game)
    deckType = CardFamily.objects.filter(game=game)
    return {
        game.title: {
            'description': game.description,
            'image': game.image.url,
            'gameBoard': {gameboard.name: gameboard.image.url for gameboard in gameBoard},
            'deckType': {decktype.id: {
                'title': decktype.title,
                'image': decktype.card_back_image.url,
                'deck_position_X': decktype.deck_position_X,
                'deck_position_Y': decktype.deck_position_Y,
                'top_left_txt': decktype.top_left_txt,
                'top_right_txt': decktype.top_right_txt,
                'bottom_left_txt': decktype.bottom_left_txt,
                'bottom_right_txt': decktype.bottom_right_txt,
                'cards': getCardsbyFamily(decktype.id)
            } for decktype in deckType},
        }
    }


def flattenList(lista: list):
    __temp_list = []
    for item in lista:
        if isinstance(item, list):
            __temp_list.extend(flattenList(item))
        else:
            __temp_list.append(item)
    return __temp_list


@api.get("/share_game/{game_id}")
def empacotarArquivos(request, game_id: int):
    '''
    Gera um dicionário estruturado com todos os arquivos para baixar.
    Chama um função que gera um empacotamento ZIP dos arquivos do jogo indicado, para o cliente baixar.
    '''
    game = Game.objects.get(id=game_id)
    gameBoard = GameBoard.objects.filter(game=game)
    deckType = CardFamily.objects.filter(game=game)

    gameboards = [gameboard.image.url for gameboard in gameBoard]
    decktypes = [decktype.card_back_image.url for decktype in deckType]
    cards = flattenList(
        [getCardsbyFamily(decktype.id, is_DLC=True) for decktype in deckType]
    )
    game_files_list = [
        game.image.url,
        *gameboards,
        *decktypes,
        *cards
    ]
    file_name = game.title.lower()
    package_data = gerarArquivo(file_name, game_files_list)
    # game.packageTimeStamp = package_data.get('time_stamp')
    
    return package_data


@api.post("/user")
def createUser(request, new_user: NewUser):
    user = User.objects.filter(username=new_user.username).first()
    if user:
        return HttpResponseForbidden('username already in use')
    user = User.objects.create_user(
        username=new_user.username, password=new_user.password, first_name=new_user.first_name)
    new_player = Jogador(
        user=user,
        avatar=new_user.avatar
    )
    new_player.save()
    # TODO: Retornar mensagem de Sucesso


@api.get("/user/{user_id}")
def userData(request, user_id: int):
    user_data = User.objects.filter(id=user_id).values(
        'id', 'last_login', 'username', 'email', 'first_name')[0]
    player_data = Jogador.objects.get(user=user_data['id'])
    user_data["last_login"] = str(user_data["last_login"])
    user_data.update({'avatar': player_data.avatar})
    if user_data["email"] != "":
        splited_email_adress = str(user_data["email"]).split('@')
        joined_email_adress = splited_email_adress[0][:3] + '*'*(
            len(splited_email_adress[0])-3) + "@" + splited_email_adress[1]
        user_data["email"] = joined_email_adress
    return user_data


@api.post("/auth")
def auth(request, user: AuthUser):
    _user = User.objects.filter(username=user.username).first()
    if _user is None:
        # TODO: retornar mensagem personalizada para cada ocorrencia
        return HttpResponseBadRequest('username not founded')
    if _user.is_active == False:
        # TODO: retornar mensagem personalizada para cada ocorrencia
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
    # TODO: retornar mensagem personalizada para cada ocorrencia
    return HttpResponseForbidden('username and password do not match')
