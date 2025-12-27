# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,x=map(int,input().split())
# a=list(map(int,input().split()))
# # s=list(input())
machines=list()
for i in range(n):
    a=list(map(int,input().split()))
    machines.append(((a[0],a[1]),(a[2],a[3])))

left=0
right=10**10
center=(left+right)//2
while abs(right-left)>1:
    money=0
    for i in range(n):
        needs=center
        first=(needs//machines[i][0][0]+min(1,needs%machines[i][0][0]))*machines[i][0][1]
        
        second=(needs//machines[i][0][0])*machines[i][0][1]
        zzz=needs-(needs//machines[i][0][0])*machines[i][0][0]
        second+=(zzz//machines[i][1][0]+min(1,zzz%machines[i][1][0]))*machines[i][1][1]
        

        third=(needs//machines[i][1][0]+min(1,needs%machines[i][1][0]))*machines[i][1][1]
        
        fourth=(needs//machines[i][1][0])*machines[i][1][1]
        yyy=needs-(needs//machines[i][1][0])*machines[i][1][0]
        fourth+=(yyy//machines[i][0][0]+min(1,yyy%machines[i][0][0]))*machines[i][0][1]
        money+=min(first,second,third,fourth)
        if money>x:
            right=center
            center=(right+left)//2
            break
    else:
        left=center
        center=(right+left)//2
print(left)