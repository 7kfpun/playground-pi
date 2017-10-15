# http://atceiling.blogspot.hk/2014/02/raspberry-pi_27.html
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

a1_pin = 14
a2_pin = 15
b1_pin = 17
b2_pin = 18

GPIO.setup(a1_pin, GPIO.OUT)
GPIO.setup(a2_pin, GPIO.OUT)
GPIO.setup(b1_pin, GPIO.OUT)
GPIO.setup(b2_pin, GPIO.OUT)

forward_seq = ['1001', '1000', '1100', '0100', '0110', '0010', '0011', '0001']
reverse_seq = forward_seq[::-1]


def forward(delay, steps):
    for i in range(steps):
        for step in forward_seq:
            set_step(step)
            time.sleep(delay)

def backwards(delay, steps):
    for i in range(steps):
        for step in reverse_seq:
            set_step(step)
            time.sleep(delay)

def set_step(step):
    GPIO.output(a1_pin, step[0] == '1')
    GPIO.output(a2_pin, step[1] == '1')
    GPIO.output(b1_pin, step[2] == '1')
    GPIO.output(b2_pin, step[3] == '1')

while True:
    set_step('0000')
    delay = input('Delay between steps (milliseconds)?')
    steps = input('How many steps forward?')
    forward(int(delay) / 1000.0, int(steps))

    set_step('0000')
    steps = input('How many steps backwards?')
    backwards(int(delay) / 1000.0, int(steps))
