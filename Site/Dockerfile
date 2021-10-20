FROM python:3.9

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python -m pip install -r requirements.txt

EXPOSE 8085

CMD ["python", "-u", "main.py"]
