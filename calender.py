import calendar
year = int(input("Enter Year:"))
month = int(input("Enter month:"))
cal = calendar.TextCalendar(calendar.MONDAY)
cal.prmonth(year, month)
