n1=int(input())
a=set(map(int,input().split()))
n2=int(input())
b=set(map(int,input().split()))
c=a.union(b)
print(len(c))