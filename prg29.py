from collections import Counter
x=int(input())
lst=list()
dct=dict()
sum=0
if 0<x<10**3:
	s=input()
	s1=s.split()
	if len(s1)==x:
		for i in s1:
			if 2<=int(i)<20:
				lst.append(int(i))
		dct=Counter(lst)
		cust=int(input())
		if 0<cust<=10**3:
			for j in range(cust):
				str1=input()
				lst2=str1.split()
				c=int(lst2[0])
				d=int(lst2[1])
				for y,z in dct.items():
					#print(y,z)
					if y==c and z>0:
						dct[y]=z-1
						sum=sum+d
				
				
				
			
print(sum)