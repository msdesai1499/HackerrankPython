def mutate_string(str1,pos,char):
	lst=list()
	str2=''
	for i in str1:
		lst.append(i)
	lst[pos]=char
	for i in lst:
		str2=str2+i
	return str2