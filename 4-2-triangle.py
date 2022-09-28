import RPi.GPIO as GPIO
import time
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
dac=[26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
period = int (input())
try:
    while True:
            for i in range(128):
                GPIO.output(dac, decimal2binary(i))
                time.sleep(period/256)
            for i in range(128,256):
                GPIO.output(dac, decimal2binary(256-i))
                time.sleep(period/256)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()