from collections import deque
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
    a=input()
    b=input()
    a_state=deque()
    b_state=deque()
    for i in a:
        if i != ')':
            a_state.append(i)
        elif len(a_state)<3:
            a_state.append(i)
        else:
            if a_state[-3]=='(' and a_state[-2]=='x' and a_state[-1]=='x':
                a_state.pop()
                a_state.pop()
                a_state.pop()
                a_state.append('x')
                a_state.append('x')
            else:
                a_state.append(i)
    for i in b:
        if i != ')':
            b_state.append(i)
        elif len(b_state)<3:
            b_state.append(i)
        else:
            if b_state[-3]=='(' and b_state[-2]=='x' and b_state[-1]=='x':
                b_state.pop()
                b_state.pop()
                b_state.pop()
                b_state.append('x')
                b_state.append('x')
            else:
                b_state.append(i)
    while a_state and b_state:
        if a_state[0]!=b_state[0]:
            print('No')
            break
        else:
            a_state.popleft()
            b_state.popleft()
    else:
        if len(a_state)==0 and len(b_state)==0:
            print('Yes')
        else:
            print('No')
