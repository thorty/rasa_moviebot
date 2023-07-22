Tutorial Source: 

https://github.com/RasaHQ/pokedex-demo

https://www.youtube.com/watch?v=sazsWmP2d3o

https://dev.to/petr7555/rasa-creating-forms-bg8

# Howto

## 1. Creating a docker image from dockerfile

### Build a dockerimage with name rasavoicedocker
docker build -t rasa3docker .

## 2. Run and use the image

### buld container
docker run --name rasa3docker -p 5002:5002 -v "${pwd}:/opt/mybot" -w "/opt/mybot" -it rasa3docker bash
### start container
docker start rasa3docker   
### get into already startet container
docker exec -it rasa3docker bash

## use rasa into container
rasa train

rasa shell

rasa run actions --actions actions --debug --auto-reload

rasa visualize 
