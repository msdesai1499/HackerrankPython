n=int(input())
name=list()
maths=list()
physics=list()
chem=list()
if 2<=n<=10:
	for i in range(0,n):
		str1=input()
		lst=str1.split()
		#print(lst,i)
		name.append(lst[0])
		maths.append(float(lst[1]))
		physics.append(float(lst[2]))
		chem.append(float(lst[3]))
		if 0<=maths[i]<=100 and 0<=physics[i]<=100 and 0<=chem[i]<=100:
			continue
		else:
			quit()
	str2=input()
	r=-1
	for i in name:
		if str2==i:
			r=name.index(i)
	if r==-1:
		quit()
	avg=(maths[r]+physics[r]+chem[r])/3
	print(format(avg, '.2f'))
	