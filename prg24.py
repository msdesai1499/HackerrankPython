def print_rangoli(n):
	width=n*4-3
	str1=''
	str2=''
	m=1
	for i in range(n,0,-1):
		str1=str1+str(i)+str1
		pattern=str1
		print(pattern.center(width,'-'))
		str1=str1[:m]
		m=m+1
	for i in range(n,1,-1):
		r=(len(pattern)//2)
		pattern=pattern[:r]+pattern[r+2:]
		print(pattern.center(width,'-'))








num=int(input())
print_rangoli(num)