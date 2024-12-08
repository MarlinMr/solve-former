FROM python:latest
WORKDIR /usr/app/src
COPY solve.py ./
CMD [ "python", "solve.py"]
