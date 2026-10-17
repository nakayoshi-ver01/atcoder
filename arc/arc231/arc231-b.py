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
# from functools import cmp_to_key, lru_cache

for _ in range(t):
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        print('Yes')
        print(0)
        print(0)
    elif a==0 and b==0 and c==1:
        print('Yes')
        print(1,1)
        print(1,1)
    elif a==0 and b==0 and c==2:
        print('Yes')
        print(2,2,3)
        print(1,2)
    elif a==0 and b==0 and c==3:
        print('No')
    elif a==0 and b==0 and c>3:
        x={1,2}
        y={1,3}
        for i in range(1,c):
            if max(x)^i!=0:
                y.add(max(x)^i)
            elif max(y)^i!=0:
                x.add(max(y)^i)
            else:
                print('No')
                break
        else:
            print('Yes')
            print(len(x),*x)
            print(len(y),*y)
    elif (a==0 or b==0) and c==0:
        print('Yes')
        x={i for i in range(a)}
        y={i for i in range(b)}
        print(len(x),*x)
        print(len(y),*y)
    elif a==0 and c>0:
        x={1}
        y={i for i in range(b)}
        if b>c:
            print('No')
            continue
        for i in range(b,c):
            if 1^i!=b:
                y.add(1^i)
            elif b^i!=0:
                x.add(b^i)
            else:
                print('No')
                break
        else:
            print('Yes')
            print(len(x),*x)
            print(len(y),*y)
    elif b==0 and c>0:
        x={i for i in range(a)}
        y={1}
        if a>c:
            print('No')
            continue
        for i in range(a,c):
            if 1^i!=a:
                x.add(1^i)
            elif a^i!=0:
                y.add(a^i)
            else:
                print('No')
                break
        else:
            print('Yes')
            print(len(x),*x)
            print(len(y),*y)
    else:
        x={i for i in range(a)}
        y={i for i in range(b)}
        z=set()
        for i in x:
            for j in y:
                z.add(i^j)
        check_num=0
        while check_num in z:
            check_num+=1
        if check_num>c:
            print('No')
        else:
            for i in range(check_num,c):
                if (a-1)^i!=b:
                    y.add((a-1)^i)
                elif (b-1)^i!=a:
                    x.add((b-1)^i)
                else:
                    print('No')
                    break
            else:
                print('Yes')
                print(len(x),*x)
                print(len(y),*y)
