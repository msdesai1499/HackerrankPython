num=int(input())
s=set(map(int,input().split()))
n=int(input())
for i in range(n):
	lst=input().split()
	if lst[0]=='pop':
		s.pop()
	elif lst[0]=='remove':
		try:
			s.remove(int(lst[1]))
		except:
			continue
	elif lst[0]=='discard':
		s.discard(int(lst[1]))
print(sum(s))
	