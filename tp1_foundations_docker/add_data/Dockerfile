# syntax=docker/dockerfile:1
FROM python:3.8

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt


RUN pip3 install -r requirements.txt
RUN apt-get -q update && apt-get -qy install netcat

COPY ./data_file_nft.csv /app
COPY ./add_data.py /app
COPY ./wait-for.sh /app

CMD ["python","-u","/app/add_data.py"]