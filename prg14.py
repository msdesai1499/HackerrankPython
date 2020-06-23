
def swap_case(str1):
	str2=''
	if 0<len(str1)<=1000:
		for i in str1:
			if i.isupper() is True:
				str2=str2+i.lower()
			elif i.islower() is True:
				str2=str2+i.upper()
			else:
				str2=str2+i
		return str2