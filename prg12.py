n=int(input())
lst=list()
for i in range(0,n):
	str1=input()
	ele=str1.split()
	if ele[0]=='insert':
		lst.insert(int(ele[1]),int(ele[2]))
	if ele[0]=='print':
		print(lst)
	if ele[0]=='remove':
		lst.remove(int(ele[1]))
	if ele[0]=='append':
		lst.append(int(ele[1]))
	if ele[0]=='sort':
		lst.sort()
	if ele[0]=='pop':
		lst.pop()
	if ele[0]=='reverse':
		lst.reverse()
	
		