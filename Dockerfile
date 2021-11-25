FROM python:3.8

ENV PYTHONBUFFERED 1

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install -r requirements.txt

CMD ["homi", "run", "-p", "8000", "app.py"]