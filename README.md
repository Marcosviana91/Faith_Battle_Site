# Faith Battle Site

## Sobre
Uma descrição voltada aos usuário pode ser encontrada na [página inicial do projeto](https://faith-battle.marcosvianadev.com.br/).

O projeto conta com uma [seção para criação de conta e edição de perfil](https://faith-battle.marcosvianadev.com.br/users), onde será possível ver conquistas, histórico de partidas, gerenciar amigos, editar deck, gerenciar jogos favoritos, entre outras idéias que sugirem.

API para login e fornecimento de JWT para autenticação em outros apps. Veremos mais a frente.

### Principais tecnologias utilizadas
- Python [Django](https://www.djangoproject.com/) - Base deste projeto.
- [Django-Ninja](https://django-ninja.dev/) - Um jeito rápido e amigável de adicionar API ao Django.
- [PostgreSQL:16](https://hub.docker.com/_/postgres) - Banco de dados containerizado em sua versão 16.
- [JWT](https://jwt.io/) - Os pacotes _passlib[argon2]_, _argon2*_ e _PyJWT_ fornecem encriptação e decriptação dos tokens fornecidos.
- Deploy em [VPS](https://www.locaweb.com.br/) e Servidor dedicado - WebServer com Gunicorn, Uvicorn e Nginx.

### Rodando o projeto
> Renomeie o arquivo [__trusted_origins_example.py](faith_battle_site/__trusted_origins_example.py) para __trusted_origins.py e adicione seus domínios caso queira.

Este projeto pode ser executado através de um container Docker `docker compose up` ou diretamente na máquina `python manage.py runserver`.
> Prefira executar o projeto em container, mas caso queira rodar o projeto direto em sua máquina é necessário ter __Python__ em sua __versão 3.12__ instalado e ambiente virtual ativado.

Acesse http://127.0.0.1:8000

> Instale a extensão [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) em seu VS Code para ver o que já está destacado no código para ser implementado.

## Acessando a API
> No [arquivo da API](faith_battle_site/api.py) é possível ver em detalhes o código e analisar as funcionalidades.  
> Acesse a API publicada do projeto para obter dados reais: https://faith-battle.marcosvianadev.com.br/api/ alterando apenas as rotas.

- GET /api/

    Retorna um dicionário com uma lista de avatares disponível para o usuário usar:
    ```JSON
    {
        "avatar_list": [
            "Abraão.jpg",
            ...
            "Sete.jpg"
        ]
    }
    ```
    > Esta rota retornará diversas informações sobre o servidor. \
    Para receber a lista de avatares use a rota  __/api/avatar_list__

- GET /api/avatar_list

    Retorna um dicionário com uma lista de avatares disponível para o usuário usar:
    ```JSON
    {
        "avatar_list": [
            "Abraão.jpg",
            ...
            "Sete.jpg"
        ]
    }
    ```

- GET /api/games

    Retorna um dicionário onde a chave é o ID do jogo cadastrado e o valor é seu nome:
    ```JSON
    {
    "1": "Faith Battle Standard"
    }
    ```

- GET /api/games/{game_id}

    Retorna retorna detalhes do jogo para serem utilizados no aplicativo, cada jogo possuirá dados distintos que serão carregados/baixados pelo app antes da partida.
    > ex.: /api/games/1
    ```JSON
    {
        "Faith Battle Standard": {
            "description": "O Faith Battle é um jogo de cartas colecionável e estratégico composto por ilustrações originais de histórias bíblicas, que tem como objetivo principal, despertar o interesse do jogador a conhecer as histórias do Livro Sagrado.",
            "image": "/media/games/faith_battle_standard.png",
            "gameBoard": {
                "Sabedoria": "/media/game_boards/faith_battle_standard_sabedoria.jpg",
                "Gelo": "/media/game_boards/faith_battle_standard_gelo.jpg"
            },
            "deckType": {
                "1": {
                    "title": "Sabedoria",
                    "image": "/media/cards/faith_battle_standard_sabedoria.png",
                    "deck_position_X": 388,
                    "deck_position_Y": 195,
                    "top_left_txt": "Pontos de Sabedoria",
                    "top_right_txt": null,
                    "bottom_left_txt": "Pontos de Ataque",
                    "bottom_right_txt": "Pontos de Defesa",
                    "cards": [
                    
                    ]
                }
            }
        }
    }
    ```
    > Os dados retornados podem não fazer sentido, dependendo do momento em que o desenvolvimento estiver. Acompanhe o desenvolvimento do aplicativo e da API [aqui](https://faith-battle.marcosvianadev.com.br/artigo/4).

- POST /api/user

    Permite criar usuários diretamente pelo aplicativo.  
    Envie o seguinte JSON no corpo da requisição:
    ```JSON
    {
        "username": "usuário_teste",
        "password": "uma_senha_qualquer",
        "first_name": "Pode Ser Seu Nome Completo",
        "avatar": "Abraão.jpg"
    }
    ```
    > O avatar deve ser um fornecido pela API em __/api/avatar_list__ .

    Não há retorno.

- GET /api/user/{user_id}

    Retorna dados do usuário:
    > ex.: /api/user/1
    ```JSON
    {
        "id": 1,
        "last_login": "2024-11-26 12:28:25.706505+00:00",
        "username": "marcosdev",
        "email": "mar*************@gmail.com",
        "first_name": "Marcos Viana",
        "avatar": "_Faith Battle.png"
    }
    ```

- POST /api/auth

    Permite autenticar usuários diretamente pelo aplicativo.  
    Envie o seguinte JSON no corpo da requisição:
    ```JSON
    {
        "username": "usuário_teste",
        "password": "uma_senha_qualquer",
    }
    ```
    Retorna um token de acesso (JWT) válido por 7 dias para usar o app sem precisar autenticar novamente.
    ```JSON
    {
        "id": integer,
        "access_token": "string"
    }
    ```