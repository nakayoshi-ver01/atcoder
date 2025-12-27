from collections import defaultdict
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
abc=defaultdict(int)
for i in range(n):
    if s[i]=='A':
        abc['a']+=1
    if s[i]=='B':
        abc['b']+=1
    if s[i]=='C':
        abc['c']+=1
ans=0
countera=[abc['a']]
if m>abc['b']:
    for i in range(abc['b']+1):
        countera.append(countera[-1]*(abc['b']-i))
    for j in range(min(m-abc['b']-1,abc['c'])):
        countera.append(countera[-1]*(abc['c']-j))
else:
    for i in range(abc['b']):
        countera.append(countera[-1]*(abc['b']-i))
print(countera)
counterb=[abc['b']]
if m>abc['a']:
    for i in range(abc['a']):
        countera.append(countera[-1]*(abc['a']-i))
    for j in range(min(m-abc['a'],abc['c'])):
        countera.append(countera[-1]*(abc['c']-j))
else:
    for i in range(abc['a']):
        countera.append(countera[-1]*(abc['a']-i))
counterc=[abc['c']]
if m>abc['c']:
    for i in range(abc['c']):
        countera.append(countera[-1]*(abc['a']-i))
    for j in range(min(m-abc['c'],abc['b'])):
        countera.append(countera[-1]*(abc['b']-j))
else:
    for i in range(abc['c']):
        countera.append(countera[-1]*(abc['c']-i))