from time import sleep
import board
from digitalio import DigitalInOut, Direction


def flash_led(num):
    if num == 1: 
        led = DigitalInOut(board.LED1)
    if num == 2: 
        led = DigitalInOut(board.LED2)
    if num == 3: 
        led = DigitalInOut(board.LED3)
    if num == 4: 
        led = DigitalInOut(board.LED4)
        
    led.direction = Direction.OUTPUT
    for i in range(10):
        if i % 2 == 0:
            led.value = True
        else:
            led.value = False
        sleep(0.5)
    led.deinit()
