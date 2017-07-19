
import datetime

#date1=datetime.datetime.now()
#print(now)
#print(now._day)
#date=datetime.datetime(date1._year,date1._month,date1._day)

'''def print_date(now1):
    date1=now1
    date2=datetime.date(,now1.month,now1.day)
    print(date2)
'''
now=datetime.date.today()
#print_date(now)
year=int(input("enter year  [YYYY]"))

date=datetime.date(year,now.month,now.day)

print(date)
