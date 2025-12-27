# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
def main():
    s=input().upper()
    t=list(input())

    for i in range(len(s)-1):
        if s[i]==t[0]:
            k=i
            break
    else:
        print('No')
        return 0
    for i in range(k+1,len(s)):
        if s[i]==t[1]:
            l=i
            break
    else:
        print('No')
        return 0

    if t[2]=='X':
        print('Yes')
        return 0
    else:
        if l==len(s):
            print('No')
            return 0
        else:
            for i in range(l+1,len(s)):
                if s[i]==t[2]:
                    print('Yes')
                    return 0
            else:
                print('No')
                return 0
            
main()