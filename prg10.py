n=int(input())
dct=dict()
lst1=list()
if 2<=n<=5:
	for i in range(0,n):
		name=input()
		marks=float(input())
		lst1.append(marks)
		dct[name]=marks
lst1.sort()
i=0
r=0.0
while True:
	if lst1[i]<lst1[i+1]:
		r=lst1[i+1]
		break
	else:
		i=i+1
lst2=list()
for x,y in dct.items():
	if y==r:
		lst2.append(x)
		
lst2.sort()
for m in lst2:
	print(m)
		
	


	