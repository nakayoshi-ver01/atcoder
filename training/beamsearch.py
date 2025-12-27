import heapq

# good_pattern=[
#     'score*-1',
#     'pattern',
#     'result'
# ]

def beamsearch(good_pattern,procedure):
    width=564
    tmp_result=[]
    for _ in range(min(len(good_pattern),width)):
        target=heapq.heappop(good_pattern)
        # 操作A
        atest_array = [i for i in target[2]]
        atest_array[procedure[0]-1]+=1
        atest_array[procedure[1]-1]+=1
        atest_array[procedure[2]-1]+=1
        # print('ggggg',atest_array)
        ascore=target[0]-atest_array.count(0)
        apattern=target[1]+['A']
        heapq.heappush(tmp_result,[ascore,apattern,atest_array])
        # print('dddddddddd',tmp_result,target)
        # 操作B
        btest_array = [i for i in target[2]]
        btest_array[procedure[0]-1]-=1
        btest_array[procedure[1]-1]-=1
        btest_array[procedure[2]-1]-=1
        bscore=target[0]-btest_array.count(0)
        bpattern=target[1]+['B']
        heapq.heappush(tmp_result,[bscore,bpattern,btest_array])
        # print('yyyyyyyyyyyyy', tmp_result,target)
    topk=[heapq.heappop(tmp_result) for _ in range(min(len(tmp_result),width))]
    return topk


t=int(input())
procedures=[list(map(int,input().split())) for _ in range(t)]
good_pattern=[[0,[],[0 for _ in range(20)]]]

for procedure in procedures:
    good_pattern=beamsearch(good_pattern, procedure)
    heapq.heapify(good_pattern)

ans=heapq.heappop(good_pattern)
for i in ans[1]:
    print(i)