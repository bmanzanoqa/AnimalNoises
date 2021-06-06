#!/bin/bash

project_name=animal_noises # by declaring a variable we can change the project name if we need to

# Build server
docker build -t ${project_name}_server server

# Build animal_api
docker build -t ${project_name}_api animal_api

# Create network (so they can talk to each other)
docker network create ${project_name}_network

# Run container
docker run -d \ # use '\' to make reading easier, it means new line
    -p 5000:5000 \
    --name ${project_name}_server \
    --network ${project_name}_network \
    ${project_name}_server # name of docker image to run the server


docker run -d \ 
    --name ${project_name}_api \
    --network ${project_name}_network \
    ${project_name}_api 