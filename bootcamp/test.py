from __future__ import print_function
import sys
import datetime

name = input("What is your name: ")


timeNow = datetime.datetime.now()

if timeNow.hour <12:
    print("Good Morning", name)
elif 12 <= timeNow.hour <18:
    print("Good Afternoon", name)
else:
    print("Good Evening", name)



