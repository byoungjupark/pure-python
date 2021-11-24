FROM python:3.8

ENV PYTHONBUFFERED 1
ENV DB_USER user
ENV DB_PASSWORD password
ENV DB_HOST localhost
ENV DB_PORT 3306
ENV DB_NAME admin

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install -r requirements.txt

CMD ["homi", "run", "-p", "8000", "app.py"]