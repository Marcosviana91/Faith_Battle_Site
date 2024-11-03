FROM python:3.12

WORKDIR /api
COPY . .

ENV TZ=America/Sao_Paulo
RUN rm -rf .venv
RUN python -m pip install -r requirements.txt

# Start Django configuration
RUN python3 manage.py collectstatic

CMD [ "gunicorn", "faith_battle_site.asgi:application", "-k", "uvicorn_worker.UvicornWorker", "-b", "0.0.0.0:3111" ]
EXPOSE 3111

