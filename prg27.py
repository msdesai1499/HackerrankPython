def merge_the_tools(str1,k):
	lst=list()
	n=len(str1)
	sub=int(n/k)
	if n%k==0 and 1<=n<=10**4 and 1<=k<=n:
		for m in range(sub):
			substr=str1[m*sub:(m+1)*sub]
			emp=""
			for i in substr:
				if i not in emp:
					emp=emp+i
			print(emp)
			
		
		
				
#str1=input()
#k=int(input())
#merge_the_tools(str1,k)
