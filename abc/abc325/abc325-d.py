from collections import defaultdict
import heapq
n=int(input())
item=list()
T=list()
st=defaultdict(list)
for i in range(n):
    p,m=map(int,input().split())
    item.append((p,p+m))
    st[p].append(p+m)
item.sort(key=lambda x:x[0])
ll=[i for i in st]
ll.sort()
cur=0
count=0
t=1

while st or T:
    if not T:
        t=ll[cur]
        get=st.pop(t)
        for i in get:
            heapq.heappush(T,i)
        cur+=1
    watch=heapq.heappop(T)
    if t<=watch:
        t+=1
        count+=1
        if t in st:
            cur+=1
            get=st.pop(t)
            for i in get:
                heapq.heappush(T,i)

print(count)