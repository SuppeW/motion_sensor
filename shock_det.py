import RPi.GPIO as GPIO
import time

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print "Movement detected"
    else:
        print "Movement detected"

GPIO.add_event_detected(channel, GPIO.BOTH, bouncetime=300)#Sier oss om pin'en går high eller overflow
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)
