# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    n,a,b=map(int,input().split())
    a-=1
    b-=1
    if n%2==1:
        print('No')
    else:
        if (a+b)%2==0:
            print('No')
        else:
            print('Yes')
            dir={'R':(0,1),'D':(1,0),'L':(0,-1),'U':(-1,0)}
            down_root=['R','D','L','D']
            up_root=['R','U','L','U']
            if b==0:
                col=0
                row=0
                step=0
                log=[]
                while col<n-1:
                    if (col+dir[down_root[step%4]][0],row+dir[down_root[step%4]][1])!=(a,b):
                        log.append(down_root[step%4])
                        col+=dir[down_root[step%4]][0]
                        row+=dir[down_root[step%4]][1]
                        step+=1
                    else:
                        log.append('D')
                        col+=1
                if row==0:
                    log.append('R')    
                log.append('R')
                print(''.join(log),end='')
                for i in range(n//2-1):
                    print('U'*(n-1),end='')
                    print('R',end='')
                    print('D'*(n-1),end='')
                    if i!=n//2-2:
                        print('R',end='')
            else:
                col=0
                row=0
                step=0
                log=[]
                while row+1!=b:
                    if row%2==0:
                        print('D'*(n-1),end='')
                        col=n-1
                    else:
                        print('U'*(n-1),end='')
                        col=0
                    print('R',end='')
                    row+=1
                if row%2==0:
                    while col<n-1:
                        if (col+dir[down_root[step%4]][0],row+dir[down_root[step%4]][1])!=(a,b):
                            log.append(down_root[step%4])
                            col+=dir[down_root[step%4]][0]
                            row+=dir[down_root[step%4]][1]
                            step+=1
                        else:
                            log.append('D')
                            col+=1
                    print(''.join(log),end='')
                    print('R',end='')
                    row+=1
                    if row<n-1:
                        print('R',end='')
                        row+=1
                        for i in range((n-row)//2):
                            print('U'*(n-1),end='')
                            print('R',end='')
                            row+=1
                            print('D'*(n-1),end='')
                            if row<n-1:
                                print('R',end='')
                                row+=1
                else:
                    while col>0:
                        if (col+dir[up_root[step%4]][0],row+dir[up_root[step%4]][1])!=(a,b):
                            log.append(up_root[step%4])
                            col+=dir[up_root[step%4]][0]
                            row+=dir[up_root[step%4]][1]
                            step+=1
                        else:
                            log.append('U')
                            col-=1
                    print(''.join(log),end='')
                    print('R',end='')
                    row+=1
                    if row<n-1:
                        print('R',end='')
                        row+=1
                        print('D'*(n-1),end='')
                        for i in range((n-row)//2):
                            print('R',end='')
                            row+=1
                            print('U'*(n-1),end='')
                            print('R',end='')
                            row+=1
                            print('D'*(n-1),end='')
            print()
        