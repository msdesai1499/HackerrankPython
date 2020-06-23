str1=input()
lst=list()
x=False
y=False
z=False
a=False
b=False
for i in str1:
	lst.append(i)
for i in lst:
	if i.isalnum():
		x=True
	if i.isalpha():
		y=True
	if i.isdigit():
		z=True
	if i.islower():
		a=True
	if i.isupper():
		b=True
print(x)
print(y)
print(z)
print(a)
print(b)