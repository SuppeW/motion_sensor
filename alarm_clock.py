import RPi.GPIO as GPIO
import time
import datetime
import os
stop = False
alarm = False
print("your alarm is set to go off at 14:20")
while stop == False:
    rn = str(datetime.datetime.now().time())
    if rn >= "16:45:00.000000":
        print(rn)
        stop = True
        while alarm == False:
              print("PLAYING LOUD MUSIC")
                GPIO.setmode(GPIO.BCM)
                    PIR_PIN = 21
                    CNT = 0;

                    GPIO.setup(PIR_PIN, GPIO.IN)

                    print "PIR Module Test (CTRL+C to exit)"
                    time.sleep(2)
                    print "Ready"


                    while True:
                        if GPIO.input(PIR_PIN):
                            CNT = CNT + 1
                            print "Motion Detected: " + str(CNT)
                            alarm = True
                        time.sleep(1)
