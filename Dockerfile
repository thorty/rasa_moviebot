FROM ubuntu:20.04

# upgrade ubuntu
RUN apt-get update && apt-get upgrade -y

# install python
RUN apt-get install -y python3.8
RUN apt-get install -y python-is-python3
RUN apt-get install python3-pip -y
RUN python -m pip install -U pip

# Install Rasa
RUN pip3 install rasa[full]==2.8.22 black==20.8b1 openpyxl pytest 