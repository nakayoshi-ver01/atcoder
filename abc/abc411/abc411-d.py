from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

# server=''
# pc=['' for _ in range(n+1)]

# for _ in range(q):
#     query=list(map(str,input().split()))
#     if query[0]=='1':
#         pc[int(query[1])]=server
#     elif query[0]=='2':
#         pc[int(query[1])]+=query[2]
#     else:
#         server=pc[int(query[1])]

# print(server)


name=defaultdict(set)
pcs=defaultdict(str)

server=''
for i in range(n):
    name[''].add(i+1)
    pcs[i+1]=''

pcs['server']=''
name[''].add('server')

for _ in range(q):
    query=list(map(str,input().split()))
    if query[0]=='1':
        name[pcs[int(query[1])]].remove(int(query[1]))
        name[pcs['server']].add(int(query[1]))
        pcs[int(query[1])]=pcs['server']
    elif query[0]=='2':
        name[pcs[int(query[1])]].remove(int(query[1]))
        name[pcs[int(query[1])]+query[2]].add(int(query[1]))
        pcs[int(query[1])]+=query[2]
    else:
        name[pcs['server']].remove('server')
        name[pcs[int(query[1])]].add('server')
        pcs['server']=pcs[int(query[1])]
        
print(pcs['server'])