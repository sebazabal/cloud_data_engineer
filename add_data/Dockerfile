# syntax=docker/dockerfile:1
FROM python:3.8

#ENTRYPOINT ["tail", "-f", "/dev/null"]

WORKDIR /app

COPY requirements.txt requirements.txt




RUN pip3 install -r requirements.txt

COPY "data_file_nft.csv" .
COPY "add_data.py" .

#COPY . .
CMD ["python3","add_data.py"]
#CMD ["python3"]




