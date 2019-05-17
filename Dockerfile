FROM python:3.6.5

RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y supervisor
RUN apt-get install -y vim
RUN apt-get install -y netcat-openbsd
RUN rm /etc/nginx/sites-available/default && rm /etc/nginx/nginx.conf

ADD . /app

COPY ./docker_files/nginx/conf.d /etc/nginx/conf.d
COPY ./docker_files/nginx/nginx.conf /etc/nginx/nginx.conf

COPY ./docker_files/supervisor/conf.d /etc/supervisor/conf.d

EXPOSE 5000

WORKDIR /app

RUN pip install -r requirements.txt
RUN chmod 700 application.py
RUN chmod 700 docker_start.sh

ENTRYPOINT ["./docker_start.sh"]
