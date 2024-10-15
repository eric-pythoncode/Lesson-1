import datetime

months = [datetime.date(2024, month, 1).strftime('%B') for month in range(1, 13)]

print("Months of each year are: ")
for month in months:
    print(month)