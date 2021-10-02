FROM python:3.9

ADD Site/requirements.txt .

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python -m pip install -r requirements.txt

EXPOSE 443

CMD ["python", "-u", "main.py"]
