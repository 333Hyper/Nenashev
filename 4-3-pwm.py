import RPi.GPIO as GPIO
pwm = 2
f = 1000
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm, GPIO.OUT)
GPIO.setup(22, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
outpwm = GPIO.PWM(pwm,f)
outpwm.start(0)
try:
    while True:
        x = int(input())
        outpwm.ChangeDutyCycle(x)
        GPIO.output(24, GPIO.input(22))
finally:
    GPIO.cleanup()