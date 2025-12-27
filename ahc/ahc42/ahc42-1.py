from collections import defaultdict,deque
from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(n)]
grid2=[list() for _ in range(n)]
huku_col=[list() for _ in range(n)]
huku_row=[list() for _ in range(n)]
huku_col2=[list() for _ in range(n)]
huku_row2=[list() for _ in range(n)]
oni_col=[list() for _ in range(n)]
oni_row=[list() for _ in range(n)]
oni_col2=[list() for _ in range(n)]
oni_row2=[list() for _ in range(n)]
ans_col=[]
ans_row=[]
for i in range(n):
    for j in range(n):
        grid2[i].append(grid[i][j])
        if grid[i][j]=='o':
            huku_row[i].append(j)
            huku_col[j].append(i)
            huku_row2[i].append(j)
            huku_col2[j].append(i)
        if grid[i][j]=='x':
            oni_row[i].append(j)
            oni_col[j].append(i)
            oni_row2[i].append(j)
            oni_col2[j].append(i)
# ans_col.append(('or',oni_row)
# ans_col.append(('oc',oni_col)

oni_count=n*2
while oni_count>0:
    oni_before=oni_count
    for i in range(n):
        flg=-1
        left_move=0
        if oni_row[i]:
            if not huku_row[i]:
                oni_left=min(oni_row[i])
                oni_right=max(oni_row[i])
                oni_count-=len(oni_row[i])
                if oni_right>n-1-oni_left:
                    for j in range(n-oni_left):
                        ans_col.append(('R',i))
                else:
                    for j in range(oni_right+1):
                        ans_col.append(('L',i))
                oni_row[i]=list()
                for j in range(n):
                    if i in oni_col[j]:
                        oni_col[j].remove(i)
            else:
                while oni_row[i]:
                    flg=0
                    left_oni=min(oni_row[i])
                    if min(huku_row[i])>left_oni:
                        oni_count-=1
                        oni_row[i].remove(left_oni)
                        oni_col[left_oni].remove(i)
                        for j in range(left_oni+1):
                            ans_col.append(('L',i))
                        left_move+=left_oni+1
                        tmp_oni=list()
                        while oni_row[i]:
                            other_oni=oni_row[i].pop()
                            oni_col[other_oni].remove(i)
                            oni_col[other_oni-left_oni-1].append(i)
                            tmp_oni.append(other_oni-left_oni-1)                        
                        oni_row[i]=list()
                        for z in tmp_oni:
                            oni_row[i].append(z)

                        tmp_huku=list()
                        while huku_row[i]:
                            other_huku=huku_row[i].pop()
                            huku_col[other_huku].remove(i)
                            huku_col[other_huku-left_oni-1].append(i)
                            tmp_huku.append(other_huku-left_oni-1)
                        huku_row[i]=list()
                        for z in tmp_huku:
                            huku_row[i].append(z)

                        flg=1    
                    if flg==0:
                        break
                
                # ans_col.append(('or',oni_row)
                # ans_col.append(('oc',oni_col)
                while oni_row[i]:
                    flg=0
                    right_oni=max(oni_row[i])
                    if max(huku_row[i])<right_oni:
                        oni_count-=1
                        oni_row[i].remove(right_oni)
                        oni_col[right_oni].remove(i)
                        for j in range(n-right_oni):
                            ans_col.append(('R',i))
                        left_move-=n-right_oni
                        tmp_oni=list()
                        while oni_row[i]:
                            other_oni=oni_row[i].pop()
                            oni_col[other_oni].remove(i)
                            oni_col[other_oni+n-right_oni].append(i)
                            tmp_oni.append(other_oni+n-right_oni)
                        oni_row[i]=[z for z in tmp_oni]

                        tmp_huku=list()
                        while huku_row[i]:
                            other_huku=huku_row[i].pop()
                            huku_col[other_huku].remove(i)
                            huku_col[other_huku+n-right_oni].append(i)
                            tmp_huku.append(other_huku+n-right_oni)
                        huku_row[i]=[z for z in tmp_huku]
                        flg=1
                    if flg==0:
                        break
            if flg!=-1:
                if left_move>0:
                    tmp_oni=list()
                    while oni_row[i]:
                        other_oni=oni_row[i].pop()
                        oni_col[other_oni].remove(i)
                        oni_col[other_oni+left_move].append(i)
                        tmp_oni.append(other_oni+left_move)
                    oni_row[i]=[z for z in tmp_oni]
                    tmp_huku=list()
                    while huku_row[i]:
                        other_huku=huku_row[i].pop()
                        huku_col[other_huku].remove(i)
                        huku_col[other_huku+left_move].append(i)
                        tmp_huku.append(other_huku+left_move)
                    huku_row[i]=[z for z in tmp_huku]
                    for _ in range(left_move):
                        ans_col.append(('R',i))
                else:
                    tmp_oni=list()
                    while oni_row[i]:
                        other_oni=oni_row[i].pop()
                        oni_col[other_oni].remove(i)
                        oni_col[other_oni+left_move].append(i)
                        tmp_oni.append(other_oni+left_move)
                    oni_row[i]=[z for z in tmp_oni]
                    tmp_huku=list()
                    while huku_row[i]:
                        other_huku=huku_row[i].pop()
                        huku_col[other_huku].remove(i)
                        huku_col[other_huku+left_move].append(i)
                        tmp_huku.append(other_huku+left_move)
                    huku_row[i]=[z for z in tmp_huku]
                    for _ in range(-left_move):
                        ans_col.append(('L',i))

    for i in range(n):
        up_move=0
        flg=-1
        if oni_col[i]:
            if not huku_col[i]:
                oni_up=min(oni_col[i])
                oni_down=max(oni_col[i])
                oni_count-=len(oni_col[i])
                if oni_down>n-1-oni_up:
                    for j in range(n-oni_up):
                        ans_col.append(('D',i))
                else:
                    for j in range(oni_down+1):
                        ans_col.append(('U',i))
                oni_col[i]=list()
                for j in range(n):
                    if i in oni_row[j]:
                        oni_row[j].remove(i)
            else:
                while oni_col[i]:
                    flg=0
                    top_oni=min(oni_col[i])
                    if min(huku_col[i])>top_oni:
                        oni_count-=1
                        oni_col[i].remove(top_oni)
                        oni_row[top_oni].remove(i)
                        for j in range(top_oni+1):
                            ans_col.append(('U',i))
                        up_move+=top_oni+1
                        tmp_oni=list()
                        while oni_col[i]:
                            other_oni=oni_col[i].pop()
                            oni_row[other_oni].remove(i)
                            oni_row[other_oni-top_oni-1].append(i)
                            tmp_oni.append(other_oni-top_oni-1)
                        oni_col[i]=[z for z in tmp_oni]

                        tmp_huku=list()
                        while huku_col[i]:
                            other_huku=huku_col[i].pop()
                            huku_row[other_huku].remove(i)
                            huku_row[other_huku-top_oni-1].append(i)
                            tmp_huku.append(other_huku-top_oni-1)
                        huku_col[i]=[z for z in tmp_huku]

                        flg=1
                    if flg==0:
                        break
                while oni_col[i]:
                    flg=0
                    down_oni=max(oni_col[i])
                    if max(huku_col[i])<down_oni:
                        oni_count-=1
                        oni_col[i].remove(down_oni)
                        oni_row[down_oni].remove(i)
                        for j in range(n-down_oni):
                            ans_col.append(('D',i))
                        up_move-=n-down_oni
                        tmp_oni=list()
                        while oni_col[i]:
                            other_oni=oni_col[i].pop()
                            oni_row[other_oni].remove(i)
                            oni_row[other_oni+n-down_oni].append(i)
                            tmp_oni.append(other_oni+n-down_oni)
                        oni_col[i]=[z for z in tmp_oni]

                        tmp_huku=list()
                        while huku_col[i]:
                            other_huku=huku_col[i].pop()
                            huku_row[other_huku].remove(i)
                            huku_row[other_huku+n-down_oni].append(i)
                            tmp_huku.append(other_huku+n-down_oni)
                        huku_col[i]=[z for z in tmp_huku]
                        flg=1
                    if flg==0:
                        break
            # if flg!=-1:
            #     if up_move>0:
            #         tmp_oni=list()
            #         while oni_col[i]:
            #             other_oni=oni_col[i].pop()
            #             oni_row[other_oni].remove(i)
            #             oni_row[other_oni+up_move].append(i)
            #             tmp_oni.append(other_oni+up_move)
            #         oni_col[i]=[z for z in tmp_oni]
            #         tmp_huku=list()
            #         while huku_col[i]:
            #             other_huku=huku_col[i].pop()
            #             huku_row[other_huku].remove(i)
            #             huku_row[other_huku+up_move].append(i)
            #             tmp_huku.append(other_huku+up_move)
            #         huku_col[i]=[z for z in tmp_huku]
            #         for _ in range(up_move):
            #             ans_col.append(('D',i))
            #     else:
            #         tmp_oni=list()
            #         while oni_col[i]:
            #             other_oni=oni_col[i].pop()
            #             oni_row[other_oni].remove(i)
            #             oni_row[other_oni+up_move].append(i)
            #             tmp_oni.append(other_oni+up_move)
            #         oni_col[i]=[z for z in tmp_oni]
            #         tmp_huku=list()
            #         while huku_col[i]:
            #             other_huku=huku_col[i].pop()
            #             huku_row[other_huku].remove(i)
            #             huku_row[other_huku+up_move].append(i)
            #             tmp_huku.append(other_huku+up_move)
            #         huku_col[i]=[z for z in tmp_huku]
            #         for _ in range(-up_move):
            #             ans_col.append(('U',i))
    # ans_col.append(('or',oni_row)
    # ans_col.append(('oc',oni_col)

oni_count=n*2
while oni_count>0:
    oni_before=oni_count
    for i in range(n):
        up_move=0
        flg=-1
        if oni_col2[i]:
            if not huku_col2[i]:
                oni_up=min(oni_col2[i])
                oni_down=max(oni_col2[i])
                oni_count-=len(oni_col2[i])
                if oni_down>n-1-oni_up:
                    for j in range(n-oni_up):
                        ans_row.append(('D',i))
                else:
                    for j in range(oni_down+1):
                        ans_row.append(('U',i))
                oni_col2[i]=list()
                for j in range(n):
                    if i in oni_row2[j]:
                        oni_row2[j].remove(i)
            else:
                while oni_col2[i]:
                    flg=0
                    top_oni=min(oni_col2[i])
                    if min(huku_col2[i])>top_oni:
                        oni_count-=1
                        oni_col2[i].remove(top_oni)
                        oni_row2[top_oni].remove(i)
                        for j in range(top_oni+1):
                            ans_row.append(('U',i))
                        up_move+=top_oni+1
                        tmp_oni=list()
                        while oni_col2[i]:
                            other_oni=oni_col2[i].pop()
                            oni_row2[other_oni].remove(i)
                            oni_row2[other_oni-top_oni-1].append(i)
                            tmp_oni.append(other_oni-top_oni-1)
                        oni_col2[i]=[z for z in tmp_oni]

                        tmp_huku=list()
                        while huku_col2[i]:
                            other_huku=huku_col2[i].pop()
                            huku_row2[other_huku].remove(i)
                            huku_row2[other_huku-top_oni-1].append(i)
                            tmp_huku.append(other_huku-top_oni-1)
                        huku_col2[i]=[z for z in tmp_huku]

                        flg=1
                    if flg==0:
                        break
                while oni_col2[i]:
                    flg=0
                    down_oni=max(oni_col2[i])
                    if max(huku_col2[i])<down_oni:
                        oni_count-=1
                        oni_col2[i].remove(down_oni)
                        oni_row2[down_oni].remove(i)
                        for j in range(n-down_oni):
                            ans_row.append(('D',i))
                        up_move-=n-down_oni
                        tmp_oni=list()
                        while oni_col2[i]:
                            other_oni=oni_col2[i].pop()
                            oni_row2[other_oni].remove(i)
                            oni_row2[other_oni+n-down_oni].append(i)
                            tmp_oni.append(other_oni+n-down_oni)
                        oni_col2[i]=[z for z in tmp_oni]

                        tmp_huku=list()
                        while huku_col2[i]:
                            other_huku=huku_col2[i].pop()
                            huku_row2[other_huku].remove(i)
                            huku_row2[other_huku+n-down_oni].append(i)
                            tmp_huku.append(other_huku+n-down_oni)
                        huku_col2[i]=[z for z in tmp_huku]
                        flg=1
                    if flg==0:
                        break
            if flg!=-1:
                if up_move>0:
                    tmp_oni=list()
                    while oni_col2[i]:
                        other_oni=oni_col2[i].pop()
                        oni_row2[other_oni].remove(i)
                        oni_row2[other_oni+up_move].append(i)
                        tmp_oni.append(other_oni+up_move)
                    oni_col2[i]=[z for z in tmp_oni]
                    tmp_huku=list()
                    while huku_col2[i]:
                        other_huku=huku_col2[i].pop()
                        huku_row2[other_huku].remove(i)
                        huku_row2[other_huku+up_move].append(i)
                        tmp_huku.append(other_huku+up_move)
                    huku_col2[i]=[z for z in tmp_huku]
                    for _ in range(up_move):
                        ans_row.append(('D',i))
                else:
                    tmp_oni=list()
                    while oni_col2[i]:
                        other_oni=oni_col2[i].pop()
                        oni_row2[other_oni].remove(i)
                        oni_row2[other_oni+up_move].append(i)
                        tmp_oni.append(other_oni+up_move)
                    oni_col2[i]=[z for z in tmp_oni]
                    tmp_huku=list()
                    while huku_col2[i]:
                        other_huku=huku_col2[i].pop()
                        huku_row2[other_huku].remove(i)
                        huku_row2[other_huku+up_move].append(i)
                        tmp_huku.append(other_huku+up_move)
                    huku_col2[i]=[z for z in tmp_huku]
                    for _ in range(-up_move):
                        ans_row.append(('U',i))
    for i in range(n):
        flg=-1
        left_move=0
        if oni_row2[i]:
            if not huku_row2[i]:
                oni_left=min(oni_row2[i])
                oni_right=max(oni_row2[i])
                oni_count-=len(oni_row2[i])
                if oni_right>n-1-oni_left:
                    for j in range(n-oni_left):
                        ans_row.append(('R',i))
                else:
                    for j in range(oni_right+1):
                        ans_row.append(('L',i))
                oni_row2[i]=list()
                for j in range(n):
                    if i in oni_col2[j]:
                        oni_col2[j].remove(i)
            else:
                while oni_row2[i]:
                    flg=0
                    left_oni=min(oni_row2[i])
                    if min(huku_row2[i])>left_oni:
                        oni_count-=1
                        oni_row2[i].remove(left_oni)
                        oni_col2[left_oni].remove(i)
                        for j in range(left_oni+1):
                            ans_row.append(('L',i))
                        left_move+=left_oni+1
                        tmp_oni=list()
                        while oni_row2[i]:
                            other_oni=oni_row2[i].pop()
                            oni_col2[other_oni].remove(i)
                            oni_col2[other_oni-left_oni-1].append(i)
                            tmp_oni.append(other_oni-left_oni-1)                        
                        oni_row2[i]=list()
                        for z in tmp_oni:
                            oni_row2[i].append(z)

                        tmp_huku=list()
                        while huku_row2[i]:
                            other_huku=huku_row2[i].pop()
                            huku_col2[other_huku].remove(i)
                            huku_col2[other_huku-left_oni-1].append(i)
                            tmp_huku.append(other_huku-left_oni-1)
                        huku_row2[i]=list()
                        for z in tmp_huku:
                            huku_row2[i].append(z)

                        flg=1    
                    if flg==0:
                        break
                
                # ans_row.append(('or',oni_row2)
                # ans_row.append(('oc',oni_col2)
                while oni_row2[i]:
                    flg=0
                    right_oni=max(oni_row2[i])
                    if max(huku_row2[i])<right_oni:
                        oni_count-=1
                        oni_row2[i].remove(right_oni)
                        oni_col2[right_oni].remove(i)
                        for j in range(n-right_oni):
                            ans_row.append(('R',i))
                        left_move-=n-right_oni
                        tmp_oni=list()
                        while oni_row2[i]:
                            other_oni=oni_row2[i].pop()
                            oni_col2[other_oni].remove(i)
                            oni_col2[other_oni+n-right_oni].append(i)
                            tmp_oni.append(other_oni+n-right_oni)
                        oni_row2[i]=[z for z in tmp_oni]

                        tmp_huku=list()
                        while huku_row2[i]:
                            other_huku=huku_row2[i].pop()
                            huku_col2[other_huku].remove(i)
                            huku_col2[other_huku+n-right_oni].append(i)
                            tmp_huku.append(other_huku+n-right_oni)
                        huku_row2[i]=[z for z in tmp_huku]
                        flg=1
                    if flg==0:
                        break
            # if flg!=-1:
            #     if left_move>0:
            #         tmp_oni=list()
            #         while oni_row2[i]:
            #             other_oni=oni_row2[i].pop()
            #             oni_col2[other_oni].remove(i)
            #             oni_col2[other_oni+left_move].append(i)
            #             tmp_oni.append(other_oni+left_move)
            #         oni_row2[i]=[z for z in tmp_oni]
            #         tmp_huku=list()
            #         while huku_row2[i]:
            #             other_huku=huku_row2[i].pop()
            #             huku_col2[other_huku].remove(i)
            #             huku_col2[other_huku+left_move].append(i)
            #             tmp_huku.append(other_huku+left_move)
            #         huku_row2[i]=[z for z in tmp_huku]
            #         for _ in range(left_move):
            #             ans_row.append(('R',i))
            #     else:
            #         tmp_oni=list()
            #         while oni_row2[i]:
            #             other_oni=oni_row2[i].pop()
            #             oni_col2[other_oni].remove(i)
            #             oni_col2[other_oni+left_move].append(i)
            #             tmp_oni.append(other_oni+left_move)
            #         oni_row2[i]=[z for z in tmp_oni]
            #         tmp_huku=list()
            #         while huku_row2[i]:
            #             other_huku=huku_row2[i].pop()
            #             huku_col2[other_huku].remove(i)
            #             huku_col2[other_huku+left_move].append(i)
            #             tmp_huku.append(other_huku+left_move)
            #         huku_row2[i]=[z for z in tmp_huku]
            #         for _ in range(-left_move):
            #             ans_row.append(('L',i))

    
    # ans_row.append(('or',oni_row2)
    # ans_row.append(('oc',oni_col2)

if len(ans_col)>len(ans_row):
    for i in ans_row:
        print(*i)
else:
    for i in ans_col:
        print(*i)