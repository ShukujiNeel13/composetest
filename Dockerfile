FROM python:3.7-alpine

WORKDIR /usr/src/composetest

RUN apk add --no-cache gcc musl-dev linux-headers
# Install gcc to speedup compilation of certain libraries.

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY . .

CMD ["flask", "run"]
