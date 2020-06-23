def print_formatted(num):
	if 1<=num<=99:
		width=len(bin(num)[2:])
		for i in range(1,num+1):
			str1=' '
			d=str(i)
			o=str(oct(i))[2:]
			h=str(hex(i))[2:]
			if h.islower()==True:
				h=h.upper()
			b=str(bin(i))[2:]
			print(d.rjust(width),o.rjust(width),h.rjust(width),b.rjust(width))
			
		