from collections import OrderedDict
lst=[str(x) for x in input()]
lst.sort()
dct=OrderedDict()
for i in lst:
	dct[i]=dct.get(i,0)+1
orders = sorted(dct.items(), key=lambda x: x[1], reverse=True)
cnt=0
for i in orders:
	if cnt==3:
		break
	print(i[0],i[1])
	cnt=cnt+1


