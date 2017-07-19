import datetime


def get_birthday():
    print("enter your birthday  ")
    year = int(input("enter year  [YYYY]  "))
    month = int(input("enter month [MM]  "))
    day = int(input("enter day  [DD]  "))
    date = datetime.date(year, month, day)
    return date


def calculate_days(now, bday):
    date1 = now
    date2 = bday

    if bday.month >= now.month:
        date2 = datetime.date(now.year, bday.month, bday.day)


    else:
        date2 = datetime.date(now.year + 1, bday.month, bday.day)
        print("your birthday will be in the year   " + str(now.year + 1))
    dt = date2 - date1
    no_of_days = int(dt.total_seconds() / 60 / 60 / 24)
    return no_of_days


def main():
    birthday = get_birthday()
    now = datetime.date.today()
    days = calculate_days(now, birthday)
    print("\n\nthe no of days left are    " + str(days))


main()
