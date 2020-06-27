t=int(input())
for _ in range(t):
	n=int(input())
	lst=list(map(int,input().split()))
	lst1=list()
	max=0
	if (lst[0]>lst[n-1]):
		max=lst[0]
	else:
		max=lst[n-1]
	while(True):
		x=1
		if not lst:
			print("Yes")
			break
		if n!=0:
			n=n-1
		if (lst[0]>lst[n]):
			lst1.append(lst[0])
			ele=lst[0]
			del lst[0]
		else:
			lst1.append(lst[n])
			ele=lst[n]
			del lst[n]
		if ele>max:
			print("No")
			break	


