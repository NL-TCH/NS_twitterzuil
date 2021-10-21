FROM python:3.9

COPY Site/. /usr/src/app
WORKDIR /usr/src/app
RUN ls
RUN pwd
RUN python -m pip install -r Site/requirements.txt

EXPOSE 8085

CMD ["python", "-u", "main.py"]
