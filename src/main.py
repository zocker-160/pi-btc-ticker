#! /usr/bin/env python3

import sys
import signal
import time

from threading import Thread
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

from lcd import LCD

API_KEY = "YOUR KEY"
API_SECRET = "YOUR SECRET"

currentPrice: float = 0

def getMethod(client: Client, lcd: LCD):
    while True:
        try:
            #client.ping()
            #price: dict = client.get_avg_price(symbol="BTCEUR")
            price: dict = client.get_symbol_ticker(symbol="BTCEUR")
        except KeyboardInterrupt:
            print("exiting....")
            sys.exit()

        lcd.writeLine2(price.get("price"))
        time.sleep(1)
        #print(price.get("price"))

def wsMethod(client: Client):
    bm = BinanceSocketManager(client)

    signal.signal(signal.SIGINT, _closeConnection)
    signal.signal(signal.SIGTERM, _closeConnection)

    bm.start_trade_socket("BTCEUR", _wsCallback)
    bm.start()

    global writeThread
    global running
    running = True
    writeThread = Thread(target=writeLCD)
    writeThread.start()

def _wsCallback(msg: dict):
    global currentPrice
    currentPrice = float(msg.get("p"))
    print(f'Preis: {msg.get("p")}')

def _closeConnection(signum, frame):
    print("exiting...")
    global running
    running = False
    reactor.stop()
    writeThread.join()

    lcd.close()

def writeLCD():
    global currentPrice
    global running

    while running:
        print(f"LCD {currentPrice}")
        lcd.writeLine2(str(currentPrice))
        time.sleep(1)


if __name__ == "__main__":
    lcd = LCD()
    client = Client(api_key=API_KEY, api_secret=API_SECRET)
    #all = client.get_all_tickers()

    # init screen
    #lcd.clear()
    lcd.writeLine1("BTC / EUR")

    #getMethod(client, lcd)
    wsMethod(client)
