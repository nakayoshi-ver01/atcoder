# n=int(input())
#n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
t=list(input())
k=['A','B','C','D','E']
p=min(abs(k.index(s[0])-k.index(s[1])),5-abs(k.index(s[0])-k.index(s[1])))
q=min(abs(k.index(t[0])-k.index(t[1])),5-abs(k.index(t[0])-k.index(t[1])))
if p==q:
    print('Yes')
else:
    print('No')