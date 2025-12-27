# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]
print(3**13)
levelcounter=[[0,0] for i in range(n+2)]
level_state=[[] for _ in range(n)]
def rec(k,now):
    global levelcounter
    global level_state
    if k==0:
        return now
    else:
        test=[]
        tmp=[]
        for i in range(len(now)):
            if now[i].count('1')>=2:
                tmp.append('1')
                levelcounter[k][1]+=1
            else:
                tmp.append('0')
                levelcounter[k][0]+=1
            if i%3==2 or k==1:
                test.append(tmp)
                tmp=[]
        print('test',test)
        level_state[k-1]=test
        d=rec(k-1,test)
    return d
test=list()
sample_ones=[0,0,0,0]
for i in range(3**(n-1)):
    sample=s[3*i:3*(i+1)]
    sample_ones[sample.count('1')]+=1
    test.append(sample)
p=rec(n,test)
print('p',p)

if p[0][0]=='1':
    pass
else:
    pass


