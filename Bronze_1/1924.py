import calendar
week_list = ['TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN', 'MON']
x, y = map(int, input().split())
print(week_list[calendar.weekday(2017, x, y)])
