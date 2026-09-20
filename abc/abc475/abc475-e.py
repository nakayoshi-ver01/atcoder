from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

t=input()

collect=defaultdict(int)
answers=[]
for i in range(n):
    sub=list(input())
    answer=[]
    check=''
    for j in range(k):
        if t[j]==sub[j]:
            check+='0'
            answer.append(0)
            collect[check]+=1
        else:
            check+='1'
            answer.append(1)
            collect[check]+=1
    answers.append(answer)
# print(collect)

q=int(input())
for _ in range(q):
    query=list(map(int,input().split()))
    query[0]-=1
    query[1]-=1
    check=''
    for j in range(k):
            check+=str(answers[query[0]][j])
            collect[check]-=1
    answers[query[0]][query[1]]=1-answers[query[0]][query[1]]
    
    check=''
    for j in range(k):
        check+=str(answers[query[0]][j])
        collect[check]+=1
    ok=0
    now=''
    while ok<m and len(now)<k:
        if collect[now+'0']+ok>m:
            now+='0'
        elif collect[now+'0']+ok==m:
            now+='0'
            print('Yes' if all(answers[query[0]][l]<=int(now[l]) for l in range(len(now))) else 'No')
            break
        else:
            ok+=collect[now+'0']
            now+='1'
    else:
        print('Yes' if ok+collect[now]<=m and any(answers[query[0]][l]==0 for l in range(len(now))) else 'No')
    # print(collect)
    # print(answers)