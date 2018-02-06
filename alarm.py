import datetime
import os
stop = False
while stop == False:
    rn = str(datetime.datetime.now().time())
    print(rn)
    if rn >= "18:00:00.000000":
        stop = True
        os.system("start BTS_House_Of_Cards.mp3")0
