"""
Problem 19: Counting Sundays
Calculates how many Sundays fell on the first of the month during the
twentieth century.
usage: python Problem19.py
"""
def LeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

def DaysInMonth(month, year):
    # April, June, September, November
    if month == 3 or month == 5 or month == 8 or month == 10:
        return 30
    elif month == 1:
        # February
        return 29 if LeapYear(year) else 28
    else:
        return 31

def AdvanceOneMonth(day, month, year):
    # move forward in day of week
    day = (day + DaysInMonth(month, year)) % 7
    # move forward in months, rolling over to new years if necessary
    month += 1
    if month == 12:
        year += 1
        month = 0

    return (day, month, year)

def main():
    month = 0
    day = 1
    year = 1900

    # move to first month of 20th century
    while year < 1901:
        day, month, year = AdvanceOneMonth(day, month, year)

    # number of Sundays on first of month
    count = 0
    # iterate over twentieth century
    while year < 2001:
        if day == 0:
            count += 1
        day, month, year = AdvanceOneMonth(day, month, year)
    print count


main()
