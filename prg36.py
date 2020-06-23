from collections import namedtuple
num=int(input())
lst=input().split()
mark=0
sum=0.00
avg=0.00
for i in range(len(lst)):
	if lst[i]=='MARKS':
		mark=i				
for i in range(num):
	lst1=input().split()
	sum=sum+int(lst1[mark])
avg=sum/num
print(round(avg,2))
	