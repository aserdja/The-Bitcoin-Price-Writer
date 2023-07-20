FROM python:3.10.12-alpine3.18

WORKDIR /app

COPY . .

RUN pip install python-binance
RUN pip install mysql-connector-python


CMD [ "python", "btc-price-logger.py" ]