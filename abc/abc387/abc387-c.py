# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
l,r=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
ans=0
if len(str(l))<len(str(r)):
    dig=list(str(l))
    for i in range(len(dig)):
        dig[i]=int(dig[i])
    for i in range(1,len(dig)):
        if dig[0]<=dig[i]:
            break
    else:
        ans=1
    for i in reversed(range(len(dig))):
        if i!=0:
            for j in range(dig[i]+1,dig[0]):
                ans+=dig[0]**(len(dig)-i-1)
        else:
            for j in range(dig[i]+1,10):
                ans+=j**(len(dig)-i-1)
    
    for i in range(len(str(l))+1,len(str(r))):
        for j in range(1,10):
            ans+=j**(i-1)
    
    rdig=list(str(r))
    for i in range(len(rdig)):
        rdig[i]=int(rdig[i])
    check=100000000
    for i in range(1,len(rdig)):
        if rdig[0]<=rdig[i]:
            check=i
            break
    else:
        ans+=1
    for i in reversed(range(len(rdig))):
        if check>=i:
            if i!=0:
                for j in range(0,min(rdig[0],rdig[i])):
                    ans+=rdig[0]**(len(rdig)-i-1)
            else:
                for j in range(1,rdig[i]):
                    ans+=j**(len(rdig)-i-1)
    print(ans)
else:
    ldig=list(str(l))
    rdig=list(str(r))
    for i in range(len(ldig)):
        ldig[i]=int(ldig[i])
        rdig[i]=int(rdig[i])
        
    check=1000000
    for i in range(len(ldig)):
        if ldig[i]<rdig[i]:
            check=i
            break
    if check==1000000:
        for i in range(1,len(rdig)):
            if rdig[0]<=rdig[i]:
                print(0)
                break
        else:
            print(1)
    else:
        ckck=100000000
        for i in range(1,len(ldig)):
            if ldig[0]<=ldig[i]:
                clcl=i
                break
        else:
            ans+=1
        for i in reversed(range(check,len(ldig))):
            if i!=check:
                for j in range(ldig[i]+1,ldig[0]):
                    ans+=ldig[0]**(len(ldig)-i-1)
            else:
                if check!=0:
                    for j in range(ldig[i]+1,rdig[i]):
                        ans+=ldig[0]**(len(ldig)-i-1)
                else:
                    for j in range(ldig[i]+1,rdig[i]):
                        ans+=j**(len(ldig)-i-1)
        for i in range(1,len(rdig)):
            if rdig[0]<=rdig[i]:
                ckck=i
                break
        else:
            ans+=1
        for i in reversed(range(check+1,len(rdig))):
            if ckck>=i:
                for j in range(0,min(rdig[0],rdig[i])):
                    ans+=rdig[0]**(len(rdig)-i-1)
        print(ans)