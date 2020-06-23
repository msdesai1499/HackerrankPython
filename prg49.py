from collections import deque
t=int(input())
d=deque()
for _ in range(t):
    lst=input().split()
    if (len(lst)>1):
        com=lst[0]
        val=int(lst[1])
    else:
        com=lst[0]
    if com=="append":
        d.append(val)
    elif com=="appendleft":
        d.appendleft(val)
    elif com=="pop":
        d.pop()
    elif com=="popleft":
        d.popleft()
str1=""
for i in d:
    str1=str1+str(i)+" "
print(str1)

