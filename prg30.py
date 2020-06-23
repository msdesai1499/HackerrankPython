from itertools import permutations
str1=input()
lst1=list()
lst2=list()
lst=str1.split()
str2=lst[0]
num=int(lst[1])
if 0<num<len(str2):
	lst1=list(permutations(str2,num))
	for i in range(len(lst1)):
		str3=''
		for k in range(num):
			str3=str3+lst1[i][k]
		lst2.append(str3)
	lst2.sort()
	for j in lst2:
		print(j)
	