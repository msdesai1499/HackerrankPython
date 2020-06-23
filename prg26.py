def minion_game(str1):
	kevin=0
	stuart=0
	if str1.isalpha():
		if 0<len(str1)<=10**6:
			for i in range(len(str1)):
				if str1[i] in 'AEIOUaeiou':
					kevin=kevin+len(str1)-i
				else:
					stuart=stuart+len(str1)-i
			if kevin>stuart:
				print('Kevin',kevin)
			elif stuart>kevin:
				print('Stuart',stuart)
			else:
				print('Draw')
			
		
str1=input()	
minion_game(str1)				
				
			