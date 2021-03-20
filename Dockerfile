FROM python:3.8

WORKDIR /server

ADD ./server /server

COPY ./requirements.txt /etc

RUN pip install -r /etc/requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]