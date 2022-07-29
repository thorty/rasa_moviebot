FROM ubuntu:20.04

# upgrade ubuntu
RUN apt-get update && apt-get upgrade -y

# install python
RUN apt-get install -y python3.8
RUN apt-get install -y python-is-python3
RUN apt-get install python3-pip -y
# install lib for visualisation
RUN python -m pip install -U pip 
RUN python -m pip install --upgrade pip


# Install Rasa
RUN pip3 install rasa[full]==3.3.1 black==20.8b1 openpyxl pytest 
#RUN pip3 install rasa[full]==3.0.10 

#for rasa-x
#RUN apt-get install -y  pkg-config libxml2-dev libxmlsec1-dev libxmlsec1-openssl libpython3.8-dev --fix-missing
#RUN pip install rasa-x --extra-index-url https://pypi.rasa.com/simple