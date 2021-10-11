import random
import calendar
import matplotlib.pyplot as plot

year = 2020
for month in [4,5,6]:
    first, end = calendar.monthrange(year, month)
    for day in range(1, end+1):
        temp = round(random.gauss(36.6,0.1), 1)
        print(f"{month}/{day} {temp}")
