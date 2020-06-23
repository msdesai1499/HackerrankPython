from collections import OrderedDict
n=int(input())
dct=OrderedDict()
for i in range(n):
	str1=input()
	if str1.islower():
		dct[str1]=dct.get(str1,0)+1
print(len(dct))
print(' '.join(str(i) for i in dct.values()))
		