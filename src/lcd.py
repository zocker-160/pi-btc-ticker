from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

class LCD:

    line1 = ""
    line2 = ""

    def __init__(self):
        self.lcd = CharLCD(pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11], numbering_mode=GPIO.BCM)

    def writeLine1(self, text: str):
        self.line1 = text
        self._toDisplay()

    def writeLine2(self, text: str):
        self.line2 = text
        self._toDisplay()

    def _toDisplay(self):
        self.clear()
        self.lcd.write_string(f"{self.line1}\n{self.line2}")

    def clear(self):
        self.lcd.clear()

    def close(self):
        self.lcd.close(clear=True)
