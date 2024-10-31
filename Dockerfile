FROM python:3.12

WORKDIR /api
COPY . .

ENV TZ=America/Sao_Paulo
RUN rm -rf .venv
RUN python -m pip install -r requirements.txt


# py manage.py runserver 0.0.0.0:3111
RUN python manage.py collectstatic

CMD [ "python", "manage.py", "runserver", "0.0.0.0:3111" ]
# CMD [ "python" ]
EXPOSE 3111

# docker build -t faith-battle-site:latest .

# docker run -d -p 3111:3111 --name faith-battle-site faith-battle-site bash
