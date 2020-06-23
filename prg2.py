num=int(input())
if 1<=num<=100:
	if num%2!=0:
		print('Weird')
	else:
		if num in range(2,6):
			print('Not Weird')
		elif num in range(6,21):
			print('Weird')
		else:
			print('Not Weird')