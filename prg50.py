import itertools as it
for i,j in it.groupby(map(int,list(input()))):
    print(tuple([len(list(j)), i]) ,end = " ")