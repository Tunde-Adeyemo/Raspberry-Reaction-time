""" YRGB.py is derived from reaction.py :
 it performs a test of the type in reaction.py for 10 times
 it then relays the result as the average and the best
 Tunde Adeyemo 01/21
 License: Public Domain """"
import time
import digitalio
import board
import random

Yed = digitalio.DigitalInOut(board.D14)
Red = digitalio.DigitalInOut(board.D15)
Ged = digitalio.DigitalInOut(board.D17)
Bed = digitalio.DigitalInOut(board.D18)
Yed.direction = digitalio.Direction.OUTPUT
Red.direction = digitalio.Direction.OUTPUT
Ged.direction = digitalio.Direction.OUTPUT
Bed.direction = digitalio.Direction.OUTPUT

bY = digitalio.DigitalInOut(board.D1)
bR = digitalio.DigitalInOut(board.D5)
bG = digitalio.DigitalInOut(board.D6)
bB = digitalio.DigitalInOut(board.D12)
bY.direction = digitalio.Direction.INPUT
bY.pull = digitalio.Pull.UP
bR.direction = digitalio.Direction.INPUT
bR.pull = digitalio.Pull.UP
bG.direction = digitalio.Direction.INPUT
bG.pull = digitalio.Pull.UP
bB.direction = digitalio.Direction.INPUT
bB.pull = digitalio.Pull.UP
stt[]

for i in range 10:

    Yed.value = False  # Start with led off
    Red.value = False
    Ged.value = False
    Bed.value = False
    time.sleep(random.random()*10)

    col = random.random() *4
    if col <1 :
        light = Yed
        button =bY
    else if col <2 and col >=1 :
        light =Red
        button =bR
    else if col <3 and col >=2 :
        light =Ged
        button =bG
    else if col >=4 :
        light =Bed
        button =bB

    light.value = True
    t0 = time.monotonic()
    while light.value == True:
        if button.value == False:
            t = time.monotonic() - t0
            print("reaction time =")
            print("%.5f " %(t))
            light.value = False
            stt.append(t)
stm = stt[0]
for i in stt:
    if i <stm :
        stm = i
    sts+=i

print("your average reaction time is")
print("%.5f " %(sts/10))
print("best reaction time is")
print("%.5f " %(stm))