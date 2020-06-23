def solve(str1):
	if 0<len(str1)<1000:
		for i in str1.split():
			str1=str1.replace(i,i.capitalize())
	return str1
	
	