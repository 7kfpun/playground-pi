# https://sites.google.com/site/raspberrypidiy/basic/gpioinput
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)

while True:
    inputValue = GPIO.input(11)

    if inputValue == False:
        print('Button pressed')
        while inputValue == False:
            inputValue = GPIO.input(11)
            time.sleep(0.3)
