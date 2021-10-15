FROM python:3.9.7

ADD Site/requirements.txt .

COPY . /usr/src/app
WORKDIR /usr/src/app
COPY Site/requirements.txt /usr/src/app
RUN pwd
RUN ls
RUN whoami
RUN python -m pip install -r /usr/src/app/requirements.txt

EXPOSE 8085

CMD ["python", "-u", "main.py"]
