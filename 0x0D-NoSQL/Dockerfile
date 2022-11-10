FROM mongo:4.2

RUN mkdir -p /home/db

COPY . /home/db

EXPOSE 27017

RUN cat 0-list_databases | mongo
