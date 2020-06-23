from collections import OrderedDict
n=int(input())
lst=list()
dct=OrderedDict()
for i in range(n):
	lst=input().split()
	for j in range(len(lst)):
		if lst[j].isdigit():
			num1=int(lst[j])
			lst.remove(lst[j])
	str1=" ".join(k for k in lst)
	if str1 in dct:
		dct[str1]=dct[str1]+num1
	else:
		dct[str1]=num1
for i,j in dct.items():
	print(i,j)