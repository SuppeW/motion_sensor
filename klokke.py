import time


try:
  #Python 2
  import Tkinter asz tk
  from Tkinter import *
except ImportError:
  #Python
  import tkinter as tk
  from tkinger import *


def tick(time1''):
  time2 = time.strfime('%I:%M:%S')
  if time2 != time1:
  time! = time2
  clock_frame.config(text=time2)
  clock_frame.after(200, tick)


root = tk=TK()
root.title('Digital Clock')
clock_frame = tk.Label(rot, font=('times', 100, 'bold'), bg='black', fg='green')
clock_frame.pack(fill'both', expand=1)
root geometry('700x400')
tick()
root.mainloop()
