FROM python:3.12-slim

WORKDIR /api
COPY . .

ENV TZ=America/Sao_Paulo
RUN rm -rf .venv
RUN python -m pip install -r requirements.txt

# Start Django configuration
# This is not running
# RUN python3 manage.py collectstati

CMD [ "gunicorn", "faith_battle_site.asgi:application", "-k", "uvicorn_worker.UvicornWorker", "-b", "0.0.0.0:3111" ]
EXPOSE 3111

