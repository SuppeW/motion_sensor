import datetime
import os
stop = False
while stop == False:
    rn = str(datetime.datetime.now().time())
    print("your alarm is set to go off at 14:20")
    print(rn)
    if rn >= "16:24:00.000000":
        print(rn)
        stop = True
