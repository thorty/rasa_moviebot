FROM ubuntu:20.04

# upgrade ubuntu
RUN apt-get update && apt-get upgrade -y

# Do this to not get stuck in timezone selection of python installation
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV DEBIAN_FRONTEND=noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# install python
RUN apt-get install -y python3.10 && apt-get install -y python-is-python3 && apt-get install -y python3-pip && apt-get install git
# install lib for visualisation
RUN python -m pip install -U pip 
RUN python -m pip install --upgrade pip


# Install Rasa
RUN pip3 install rasa[full]==3.6.2 black==20.8b1 openpyxl pytest pandas
RUN pip3 install pymilvus==2.2.14

#for rasa-x -does not work with rasa3
#ENV DEBIAN_FRONTEND=noninteractive
#RUN apt-get update
#RUN apt-get -y install tzdata
#RUN apt-get install -y  pkg-config libxml2-dev libxmlsec1-dev libxmlsec1-openssl libpython3.8-dev --fix-missing
#RUN pip install rasa-x --extra-index-url https://pypi.rasa.com/simple