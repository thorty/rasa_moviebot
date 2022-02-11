# Howto

## 1. Creating a docker image from dockerfile

### Choose rasa_gpu.dockerfile or rasa_cpu.dockerfile and copy it as Dockerfile.
cp rasa_cpu.dockerfile Dockerfile
### Build a dockerimage with name rasavoicedocker
docker build -t rasavoicedocker .

## 2. Run and use the image

###
docker run --name localRasa -v "${pwd}:/opt/mybot" -w "/opt/mybot" -it rasavoicedocker bash
docker exec -v "${pwd}:/opt/mybot" -w "/opt/mybot" -it localRasa bash

### training
docker run --name localRasa -v "${pwd}:/opt/fragmagentarasamodel" -w "/opt/fragmagentarasamodel" rasavoicedocker rasa train

### run action server
docker run --name localRasa -v "${pwd}:/opt/rasa-action-server" -w "/opt/rasa-action-server"" rasavoicedocker rasa run actions --actions actions --debug --auto-reload`

### running shell
docker run -it --name localRasa -v "${pwd}:/opt/fragmagentarasamodel" -w "/opt/fragmagentarasamodel" rasavoicedocker rasa shell



