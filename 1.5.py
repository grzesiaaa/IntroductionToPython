import datetime

run = datetime.timedelta(hours = 6, minutes = 52)
recreation = datetime.timedelta(minutes = 6, seconds = 15)
fast = datetime.timedelta(minutes = 4, seconds = 12)

print(run + 1.5*recreation + 4.8*fast + 1*recreation)
