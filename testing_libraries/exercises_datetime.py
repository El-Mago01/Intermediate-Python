import datetime as dt
import time as t
import statistics

# print the current date:
hoje=dt.date.today()
print("Today's date: ",hoje)

#print the current time:
current_time = t.localtime(t.time())
print(t.strftime("%H:%M:%S", current_time))

#print the current month as a string
current_time = dt.date.today()
formatted_date=current_time.strftime("%B")
print(formatted_date)

#Bonus1: Create a datetime object representing Lee's birth date (04.07.2001)
lee_birthdate=dt.datetime(2001,7,4)
print("The birthday of Lee was in week: ", lee_birthdate.strftime("%U"))
today_dt=dt.datetime.today()
difference=dt.datetime.now()-lee_birthdate
print(difference.days / 365)

#get the median of a list of grades:

grades = [50, 20, 35, 40, 100, 5, 100]

grades_median=statistics.median(grades)
print(grades_median)

#Bonus2: calculate how many hours it has been since Lee was born
#assuming Lee’s birthdate and time is “2001-07-04 14:30:00”.
# Print the total number of hours in the following format: “X hours since Lee was born.”
lee_birthdate = dt.datetime(2001, 7, 4, 14, 30)
right_now=dt.datetime.now()
difference=right_now-lee_birthdate
print("The difference in hours: ",difference.seconds/3600)

#About timezones:
