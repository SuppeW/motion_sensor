import datetime
import os
stop = False
print("your alarm is set to go off at 14:20")
while stop == False:
    rn = str(datetime.datetime.now().time())
    if rn >= "16:44:00.000000":
        print(rn)
        stop = True
