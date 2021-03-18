from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

class LCD:

    def __init__(self):
        self.lcd = CharLCD(pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11], numbering_mode=GPIO.BCM)

    def writeLine1(self, text: str):
        self.clear()
        self.lcd.write_string(f"{text}")

    def writeLine2(self, text: str):
        self.clear()
        self.lcd.write_string(f"\n{text}")

    def clear(self):
        self.lcd.clear()

    def close(self):
        self.lcd.close(clear=True)
