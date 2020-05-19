FROM ubuntu

MAINTAINER Vikrant "viku1996@gmail.com"

RUN apt-get update -y

RUN apt-get install -y python3

RUN apt-get update -y

RUN apt-get upgrade -y

RUN apt-get install -y python3-pip 

RUN apt-get install -y build-essential libssl-dev libssl-dev libffi-dev python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
