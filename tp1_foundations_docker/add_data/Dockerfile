# syntax=docker/dockerfile:1
FROM python:3.8

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt


RUN pip3 install -r requirements.txt

COPY ./data_file_nft.csv /app
COPY ./add_data.py /app

CMD ["python","-u", "/app/add_data.py"]