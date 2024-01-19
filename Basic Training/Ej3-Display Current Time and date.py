#Write a Python program to display the current date and time

import  datetime

date = datetime.datetime.now()

print("Current date and time is:\n",date.strftime("%Y-%m-%d %H:%M:%S"))