from datetime import date, datetime
#get today's date
today = date.today()

#get current date and time
now = datetime.now()

#Display results

print("Today's date is : ",today)
print("The time is : ",now)

#Display date components
print("Year : ",today.year)
print("Month : ",today.month)
print("Date : ",today.day)