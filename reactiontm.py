# instant.py : to determine the lag time between signal and
# reception when the button is pressed
# Tunde Adeyemo 01/21
# License: Public Domain
import time
import digitalio
import board
import random

led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

t = 0.0
inct = 0.0002

led.value = False  # Start with led off
pause(random()*10)
t0 = time.monotonic()
led.value = True
while led.value == True:
    if button.value == True:
        print("reaction time = %.4f " %(time.monotonic - t0))
        led.value = False