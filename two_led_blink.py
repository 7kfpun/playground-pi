# https://sites.google.com/site/raspberrypidiy/basic/gpioled
import RPi.GPIO as GPIO
from gpiozero import Button, LED
from time import sleep

from signal import pause

red_led = LED(17)
green_led = LED(18)

button = Button(2)

try:
    button.when_pressed = red_led.on
    button.when_released = red_led.off

    while True:
        red_led.on()
        green_led.off()
        sleep(1)
        red_led.off()
        green_led.on()
        sleep(1)
except KeyboardInterrupt:
    print('end')
finally:
    GPIO.cleanup()
