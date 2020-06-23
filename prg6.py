def is_leap(year):
	l=False
	if year%4==0:
		l=True
	if year%100==0:
		l=False
	if year%400==0:
		l=True
	return l

		
	