import time
import board
import digitalio
import usb_midi
import adafruit_midi  # MIDI protocol encoder/decoder library
from adafruit_midi.control_change import ControlChange #control_change
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)# Write your code here :-)

button1 = digitalio.DigitalInOut(board.GP10)
button1.switch_to_input(pull=digitalio.Pull.UP)
button2 = digitalio.DigitalInOut(board.GP11)
button2.switch_to_input(pull=digitalio.Pull.UP)
button3 = digitalio.DigitalInOut(board.GP12)
button3.switch_to_input(pull=digitalio.Pull.UP)
button4 = digitalio.DigitalInOut(board.GP13)
button4.switch_to_input(pull=digitalio.Pull.UP)
button5 = digitalio.DigitalInOut(board.GP14)
button5.switch_to_input(pull=digitalio.Pull.UP)
button6 = digitalio.DigitalInOut(board.GP15)
button6.switch_to_input(pull=digitalio.Pull.UP)
button7 = digitalio.DigitalInOut(board.GP16)
button7.switch_to_input(pull=digitalio.Pull.UP)
button8 = digitalio.DigitalInOut(board.GP17)
button8.switch_to_input(pull=digitalio.Pull.UP)

led1 = digitalio.DigitalInOut(board.GP2)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP3)
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(board.GP4)
led3.direction = digitalio.Direction.OUTPUT
led4 = digitalio.DigitalInOut(board.GP5)
led4.direction = digitalio.Direction.OUTPUT
led5 = digitalio.DigitalInOut(board.GP6)
led5.direction = digitalio.Direction.OUTPUT
led6 = digitalio.DigitalInOut(board.GP7)
led6.direction = digitalio.Direction.OUTPUT
led7 = digitalio.DigitalInOut(board.GP8)
led7.direction = digitalio.Direction.OUTPUT
led8 = digitalio.DigitalInOut(board.GP9)
led8.direction = digitalio.Direction.OUTPUT

flag1 = 1
flag2 = 1
flag3 = 1
flag4 = 1
flag5 = 1
flag6 = 1
flag7 = 1
flag8 = 1


while True:
    if not button1.value and flag1 != 0:
        midi.send(ControlChange(1, 127))
        print("LED1 ON")
        led1.value = True
        flag1 = 0
        time.sleep(0.75)
    elif not button1.value and flag1 != 1:
        midi.send(ControlChange(1, 0))
        led1.value = False
        print("LED1 off ")
        flag1 = 1
        time.sleep(0.75)
    if not button2.value and flag2 != 0:
        midi.send(ControlChange(2, 127))
        print("LED2 ON")
        led2.value = True
        flag2 = 0
        time.sleep(0.75)
    elif not button2.value and flag2 != 1:
        midi.send(ControlChange(2, 0))
        led2.value = False
        print("LED2 off ")
        flag2 = 1
        time.sleep(0.75)
    if not button3.value and flag3 != 0:
        midi.send(ControlChange(3, 127))
        print("LED3 ON")
        led3.value = True
        flag3 = 0
        time.sleep(0.75)
    elif not button3.value and flag3 != 1:
        midi.send(ControlChange(3, 0))
        led3.value = False
        print("LED3 off ")
        flag3 = 1
        time.sleep(0.75)
    if not button4.value and flag4 != 0:
        midi.send(ControlChange(4, 127))
        print("LED4 ON")
        led4.value = True
        flag4 = 0
        time.sleep(0.75)
    elif not button4.value and flag4 != 1:
        midi.send(ControlChange(4, 0))
        led4.value = False
        print("LED4 off ")
        flag4 = 1
        time.sleep(0.75)
    if not button5.value and flag5 != 0:
        midi.send(ControlChange(5, 127))
        print("LED5 ON")
        led5.value = True
        flag5 = 0
        time.sleep(0.75)
    elif not button5.value and flag5 != 1:
        midi.send(ControlChange(5, 0))
        led5.value = False
        print("LED5 off ")
        flag5 = 1
        time.sleep(0.75)
    if not button6.value and flag6 != 0:
        midi.send(ControlChange(6, 127))
        print("LED6 ON")
        led6.value = True
        flag6 = 0
        time.sleep(0.75)
    elif not button6.value and flag6 != 1:
        midi.send(ControlChange(6, 0))
        led6.value = False
        print("LED6 off ")
        flag6 = 1
        time.sleep(0.75)
    if not button7.value and flag7 != 0:
        midi.send(ControlChange(7, 127))
        print("LED7 ON")
        led7.value = True
        flag7 = 0
        time.sleep(0.75)
    elif not button7.value and flag7 != 1:
        midi.send(ControlChange(7, 0))
        led7.value = False
        print("LED7 off ")
        flag7 = 1
        time.sleep(0.75)
    if not button8.value and flag8 != 0:
        midi.send(ControlChange(8, 127))
        print("LED8 ON")
        led8.value = True
        flag8 = 0
        time.sleep(0.75)
    elif not button8.value and flag8 != 1:
        midi.send(ControlChange(8, 0))
        led8.value = False
        print("LED8 off ")
        flag8 = 1
        time.sleep(0.75)
