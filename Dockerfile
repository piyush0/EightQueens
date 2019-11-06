FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
CMD python ./main.py