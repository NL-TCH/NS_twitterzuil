FROM python:3.9

ADD Site/requirements.txt .

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python3 pip install requirements.txt

EXPOSE 443

CMD ["python", "-u", "main.py"]
