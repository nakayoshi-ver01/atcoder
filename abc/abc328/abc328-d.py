from collections import deque
s=list(input())
t=deque()
ans=str()
for i in s:
    t.append(i)
    if len(t)>=3:
        if t[-1]=='C' and t[-2]=='B' and t[-3]=='A':
            for i in range(3):
                t.pop()
for j in range(len(t)):
    ans+=t.popleft()
print(ans)