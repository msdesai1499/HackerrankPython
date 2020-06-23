n=int(input())
str1=input()
tup=tuple(map(int,str1.split()))
if len(tup)==n:
	print(hash(tup))
else:
	quit()