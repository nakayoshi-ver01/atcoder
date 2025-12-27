from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
t=list(input())
# grid=[list(input()) for _ in range(h)]
def solve(n,s,t):
    s_char_set=defaultdict(set)
    t_char_set=defaultdict(set)
    for i in range(n):
        s_char_set[s[i]].add(i)
        t_char_set[t[i]].add(i)

    used=defaultdict(bool)
    s_to_t=defaultdict(set)
    for i in s_char_set:
        for j in t_char_set:
            if i!=j and s_char_set[i].issubset(t_char_set[j]):
                s_to_t[j].add(i)
                used[i]=True
                used[j]=True
            elif i!=j and t_char_set[j].issubset(s_char_set[i]):
                return -1



    # print(s_to_t)
    komoji=[chr(i) for i in range(97,123)]
    full_flg=True
    for i in komoji:
        if not used[i]:
            full_flg=False
            break

    komoji_flg=defaultdict(bool)
    states=deque()
    s_keys=set(s_char_set.keys())
    t_keys=set(t_char_set.keys())
    if len(s_keys-t_keys)>0 or len(t_keys)<26:
        free_char=True
    else:
        free_char=False
    # print(t_keys)
    start_keys=t_keys-s_keys
    if start_keys:
        x=start_keys.pop()
        states.append((1,x))
        t_keys.remove(x)
        komoji_flg[x]=True
    else:
        if free_char:
            x=t_keys.pop()
            states.append((1,x))
            komoji_flg[x]=True
        else:
            return -1

    ans=0
    
    while t_keys or states:
        if not states:
            if start_keys:
                x=start_keys.pop()
                states.append((1,x))
                t_keys.remove(x)
                komoji_flg[x]=True
            else:
                x=t_keys.pop()
                states.append((1,x))
                komoji_flg[x]=True
                
        now=states.popleft()
        for i in s_to_t[now[1]]:
            if not komoji_flg[i]:
                komoji_flg[i]=True
                states.append((now[0]+1,i))
                if i in t_keys:
                    t_keys.remove(i)
                ans+=1
            else:
                ans+=2
        # print(now,ans,states)
    return ans

print(solve(n,s,t))