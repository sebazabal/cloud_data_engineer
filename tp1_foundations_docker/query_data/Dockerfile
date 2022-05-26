# syntax=docker/dockerfile:1
FROM python:3.8

#ENTRYPOINT ["tail", "-f", "/dev/null"]

WORKDIR /app_query

ADD ./requirements.txt /app_query/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./query.py /app_query

#COPY . .
CMD ["python","-u","/app_query/query.py","tail","-f","/dev/null"]

#"-u" libera el buffer el I/O de la terminal
