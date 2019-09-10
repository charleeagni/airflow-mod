# Building master
docker build -t airflow-master /root/airflow-master
docker build -t airflow-rabbitmq /root/airflow-rabbitMQ
# Running the docker images
docker run -it --network my-attachable-overlay airflow-master:latest

docker run -d --name scheduler --network my-attachable-overlay airflow-master:latest scheduler
docker run -d --name worker --network my-attachable-overlay airflow-master:latest worker


# Rabbitmq
docker run -it --network my-attachable-overlay airflow-rabbitmq:latest
docker run --name rabbit -d -p 5672:5672 -p 15672:15672 --network my-attachable-overlay airflow-rabbitmq:latest

# create postgress image
docker run --name posttest -d -p 5432:5432 -e POSTGRES_PASSWORD=fred --network my-attachable-overlay postgres:alpine

docker network create -d overlay --attachable my-attachable-overlay
