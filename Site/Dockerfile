FROM python:3.9

ADD Site/requirements.txt .

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pwd
RUN ls
RUN whoami
RUN cat requirements.txt
RUN python -m pip install -r Site/requirements.txt

EXPOSE 443

CMD ["python", "-u", "main.py"]
