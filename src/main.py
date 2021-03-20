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

class Ticker:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

        print("init BTC ticker...")
        self.lcd = LCD()
        self.client = Client(api_key=API_KEY, api_secret=API_SECRET)

        # init screen
        self.lcd.clear()
        self.lcd.writeLine1("BTC / EUR")

        self.running: bool = False
        self.currentPrice: float = 0

    def getMethod(self):
        """ Poll price by sending an active request to the binance server """
        while True:
            try:
                #client.ping()
                #price: dict = client.get_avg_price(symbol="BTCEUR")
                price: dict = self.client.get_symbol_ticker(symbol=self.symbol)
            except KeyboardInterrupt:
                print("exiting....")
                sys.exit()

            self.lcd.writeLine2(price.get("price"))
            time.sleep(1)
            #print(price.get("price"))

    def wsMethod(self):
        """ Get current price by using a websocket connection """
        bm = BinanceSocketManager(self.client)

        signal.signal(signal.SIGINT, self._closeConnection)
        signal.signal(signal.SIGTERM, self._closeConnection)

        bm.start_trade_socket(self.symbol, self._wsCallback)
        bm.start()

        self.running = True
        self.writeThread = Thread(target=self.writeLCD)
        self.writeThread.start()

    def _wsCallback(self, msg: dict):
        self.currentPrice = float(msg.get("p"))
        print(f'Preis: {self.currentPrice}')

    def writeLCD(self):
        while self.running:
            print(f"LCD {self.currentPrice}")
            self.lcd.writeLine2(str(self.currentPrice))
            time.sleep(1)

    def _closeConnection(self, signum, frame):
        print("exiting...")
        self.running = False
        reactor.stop()
        self.writeThread.join()

        self.lcd.close()    

if __name__ == "__main__":
    tc = Ticker("BTCEUR")
    tc.wsMethod()
