from collections import defaultdict
n,m=map(int,input().split())
lst1=list()
lst2=list()
dct=defaultdict(list)
if 1<=n<=10000 and 1<=m<=100:
	for i in range(n):
		lst1.append(input())
	for j in range(m):
		lst2.append(input())
	#print(lst1,lst2)
	for i in range(n):
		for j in lst2:
			if lst1[i]==j:
				dct[j].append(i+1)
	for j in lst2:
		if j not in dct.keys():
			dct[j].append(-1)
	for i in dct.keys():
		str2=''
		for j in dct[i]:
			str2=str2+str(j)+' '
		print(str2)
			
	
	