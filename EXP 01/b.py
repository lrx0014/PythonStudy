from _datetime import datetime, timedelta

today = datetime.today();
print(today)
yesterday=today-timedelta(days=1)
print(yesterday)

