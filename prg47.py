m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
c=a.intersection(b)
d=a.union(b)
e=d.difference(c)
f=list(e)
f.sort()
for i in f:
	print(i)