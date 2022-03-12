Tutorial Source: https://github.com/RasaHQ/pokedex-demo
https://www.youtube.com/watch?v=sazsWmP2d3o

next step use slots to store info: 
1. ask if user wants mor info about choosen pokemon
2. ask which info
3. fetch and play info
https://www.google.com/search?client=firefox-b-d&q=use+slots+in+rasa#kpvalbx=_2MwGYrehOdbi7_UP2pmq2AU17

-- what if user asks other questions?...

# Howto

## 1. Creating a docker image from dockerfile

### Choose rasa_gpu.dockerfile or rasa_cpu.dockerfile and copy it as Dockerfile.
cp rasa_cpu.dockerfile Dockerfile
### Build a dockerimage with name rasavoicedocker
docker build -t rasavoicedocker .

## 2. Run and use the image

### buld container
docker run --name localRasa -v "${pwd}:/opt/mybot" -w "/opt/mybot" -it rasavoicedocker bash
### start container
docker start localRasa   
### get into already startet container
docker exec -it localRasa bash

## use rasa into container
rasa train 
rasa shell
rasa run actions --actions actions --debug --auto-reload







