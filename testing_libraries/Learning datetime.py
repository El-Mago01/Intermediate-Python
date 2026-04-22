import datetime as dt
import pytz

#get the current time in Berlin timezone in var dt_berlin

tz=pytz.timezone('Europe/Berlin')
dt_utcnow=dt.datetime.now(pytz.utc)
dt_berlin=dt_utcnow.astimezone(tz) #this one is offset aware

print(dt_berlin.time())
print(dt_utcnow.time())

#construct a new date:birthday
b_day=dt.datetime(1969,8,15) #this one is offset naive
b_day_aware=tz.localize(b_day) #this one is offset aware
days_until_b_day=b_day_aware.replace(year=2026) - dt_berlin # You can only substract aware-aware
print(days_until_b_day)


#Bonus question5
#calculate the hours since the birth of Lee (2001-07-04 14:30:00)
tz=pytz.timezone('Europe/Berlin')
b_day=dt.datetime(2001,7,4,14,30,0)
b_day_aware=tz.localize(b_day)

t_day=dt.datetime.now()
t_day_aware=tz.localize(t_day)

dt_since_birth=t_day_aware - b_day_aware
#print(dt_since_birth, t_day_aware, b_day_aware)
hours_since_birth=dt_since_birth.total_seconds() / 3600
print(type(dt_since_birth))
print(f"{int(hours_since_birth)} hours since Lee was born.")