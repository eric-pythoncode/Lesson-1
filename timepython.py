import datetime

now = datetime.datetime.now()

currentdate = now.strftime("%Y-%m-%d")
currenttime = now.strftime("%H:%M:%S")
currenttime1 = now.strftime("%I:%M:%S")

print("Current date: ", currentdate)
print("Current time (military): ", currenttime)
print("Current time: ", currenttime1)