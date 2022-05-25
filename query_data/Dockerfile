# syntax=docker/dockerfile:1
FROM python:3.8

#ENTRYPOINT ["tail", "-f", "/dev/null"]

WORKDIR /app_query

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY query.py query.py
#COPY . .
CMD ["python","-u","query.py"]

