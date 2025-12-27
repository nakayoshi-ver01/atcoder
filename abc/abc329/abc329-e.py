from collections import defaultdict
# n=int(input())
n,q=map(int,input().split())
y=list(map(int,input().split()))
boxes=defaultdict(set)
que=list()
pri=set()
for i in range(n):
    boxes[i+1].add(y[i])
for _ in range(q):
    que.append(map(int,input().split()))
for i in range(q):
    a,b=que[i]
    if len(boxes[b])>=len(boxes[a]):
        boxes[b]|=boxes[a]
        boxes[a].clear()
    else:
        boxes[a]|=boxes[b]
        boxes[a],boxes[b]=boxes[b],boxes[a]
        boxes[a].clear()
    print(len(boxes[b]))