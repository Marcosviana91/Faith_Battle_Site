FROM python:3.12-slim

WORKDIR /api
COPY . .

ENV TZ=America/Sao_Paulo

RUN python -m pip install -r requirements.txt

CMD [ "gunicorn", "faith_battle_site.asgi:application", "-k", "uvicorn_worker.UvicornWorker", "-b", "0.0.0.0:8000" ]
# CMD [ "gunicorn", "faith_battle_site.asgi:application", "-k", "uvicorn_worker.UvicornWorker", "-b", "unix:/api/sockets/faith_battle_site.sock" ]

