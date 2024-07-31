from datetime import datetime

now = datetime.now()

print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.timestamp())

print(now.strftime("%m/%d/%Y, %H:%M:%S"))

s_date = '5 December, 2019'

print(datetime.strptime(s_date, "%d %B, %Y"))

new_year = datetime(year=2025, month=1, day=1, hour=0, minute=0, second=0)

print(new_year - now)

begin_year = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)

print(now - begin_year)
