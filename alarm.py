import datetime
import os
stop = False
aTime = 18:00:00.000000
while stop == False:
    rn = str(datetime.datetime.now().time())
    print("Your alarm is set to go off at: "aTime)
    if rn >= aTime:
        stop = True
