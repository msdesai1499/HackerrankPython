import calendar
mon,day,year=map(int,input().split())
if 2000<year<3000:
	daynum=calendar.weekday(year,mon,day)
	days=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
	print(days[daynum])
