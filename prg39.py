import re
t=int(input())
if 0<t<100:
	for i in range(t):
		str1=input()
		try:
			re.compile(str1)
			is_valid = True
		except re.error:
			is_valid = False
		print(is_valid)
	