#!/usr/bin/env bash


option=$1
if [[ "$option" = "c" ]]; then 
    # Kill all the containers and clean them up
    docker kill $(docker ps -q)
     docker rm $(docker ps -a -q)
else
cd ./consul_servers && docker-compose up 


fi