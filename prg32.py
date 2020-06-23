from itertools import combinations_with_replacement
str1=input().split()
num=int(str1[1])
str2=str1[0]
if 0<num<=len(str2) and str2.isupper()==True:
	for j in combinations_with_replacement(sorted(str2),num):
		print(''.join(j))
	