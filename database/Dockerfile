FROM postgres:14
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=dbname
COPY init.sql /docker-entrypoint-initdb.d/
EXPOSE 5432