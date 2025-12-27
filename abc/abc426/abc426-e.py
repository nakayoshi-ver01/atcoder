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
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if (a[0]-a[2])**2+(a[1]-a[3])**2>(b[0]-b[2])**2+(b[1]-b[3])**2:
        longer=a[::]
        shorter=b[::]
    else:
        longer=b[::]
        shorter=a[::]
    
    vsx=(shorter[0]-shorter[2])/(((shorter[0]-shorter[2])**2+(shorter[1]-shorter[3])**2)**(1/2))
    vsy=(shorter[1]-shorter[3])/(((shorter[0]-shorter[2])**2+(shorter[1]-shorter[3])**2)**(1/2))
    vlx=(longer[0]-longer[2])/(((longer[0]-longer[2])**2+(longer[1]-longer[3])**2)**(1/2))
    vly=(longer[1]-longer[3])/(((longer[0]-longer[2])**2+(longer[1]-longer[3])**2)**(1/2))

    ts=(((shorter[0]-shorter[2])**2+(shorter[1]-shorter[3])**2)**(1/2))
    tl=(((longer[0]-longer[2])**2+(longer[1]-longer[3])**2)**(1/2))

    dx=(shorter[0]-longer[0])
    dy=(shorter[1]-longer[1])

    vx=(vsx-vlx)
    vy=(vsy-vly)

    axis=(dx*vx+dy*vy)/(vx**2+vy**2)

    if 0<=axis<=ts:
        a_1=dx**2+dy**2-(dx*vx+dy*vy)**2/(vx**2+vy**2)
    elif axis<=0:
        a_1=dx**2+dy**2
    else:
        a_1=((ts+(dx*vx+dy*vy)/(vx**2+vy**2))**2)*(vx**2+vy**2)+dx**2+dy**2-(dx*vx+dy*vy)**2/(vx**2+vy**2)
    
    a_2=0

    dzx=(shorter[2]-longer[0]-ts*vlx)
    dzy=(shorter[3]-longer[1]-ts*vly)
    vzx=-vlx
    vzy=-vly

    axis_2=(dzx*vzx+dzy*vzy)/(vzx**2+vzy**2)
    if ts<=axis_2<=tl:
        a_2=dzx**2+dzy**2-(dzx*vzx+dzy*vzy)**2/(vzx**2+vzy**2)
    elif axis_2<=ts:
        a_2=dzx**2+dzy**2
    else:
        a_2=((ts+(dzx*vzx+dzy*vzy)/(vzx**2+vzy**2))**2)*(vzx**2+vzy**2)+dzx**2+dzy**2-(dzx*vzx+dzy*vzy)**2/(vzx**2+vzy**2)
    
    print(a_1,a_2)