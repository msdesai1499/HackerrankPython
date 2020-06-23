n=int(input())
lst=list()
if 2<=n<=10:
	num=input()
	num1=num.split()
	for i in num1:
		num=int(i)
		if -100<=num<=100:
			lst.append(num)
lst.sort(reverse=True)
i=0
while True:
	if lst[i]>lst[i+1]:
		print(lst[i+1])
		break
	else:
		i=i+1
			
			