import RPi.GPIO as GPIO
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
dac=[26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
try:
    while True:
        a = input()
        if a.isdigit():
            if int(a)>255 or int(a)<0:
                print('Not allowed data')
            else:
                GPIO.output(dac, decimal2binary(int(a)))
                result = (3.3 / 256) * int (a)
                print("выходное напряжение ", end="")
                print(f'{result:.{4}f}')
        elif a=="q":
            break
        else:
            print('Not allowed data')
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
