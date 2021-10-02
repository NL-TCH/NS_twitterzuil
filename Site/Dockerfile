FROM python:3.9

ADD requirements.txt .

COPY . /usr/src/app
WORKDIR /usr/src/app
COPY Site/requirements.txt .
RUN pwd
RUN ls
RUN whoami
RUN cat requirements.txt
RUN python -m pip install -r requirements.txt

EXPOSE 443

CMD ["python", "-u", "main.py"]
