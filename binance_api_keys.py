from binance.client import Client
import os

BINANCE_API_KEY = os.environ.get("BINANCE_API_KEY")
BINANCE_SECRET_API_KEY = os.environ.get("BINANCE_SECRET_API_KEY")

binance_client = Client(BINANCE_API_KEY, BINANCE_SECRET_API_KEY)
