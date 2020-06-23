from itertools import product
str1=input()
str2=input()
lst1=str1.split()
map1=map(int,lst1)
lst1=list(map1)
lst2=str2.split()
map2=map(int,lst2)
lst2=list(map2)
lst3=list(product(lst1,lst2))
str3=""
for i in lst3:
	str3=str3+str(i)+' '
print(str3)