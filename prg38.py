t=int(input())
if 0<t<10:
	for i in range(t):
		try:
			a,b=map(int,input().split())
			c=a//b
			print(c)
		except Exception as e:
			print('Error Code:',e)