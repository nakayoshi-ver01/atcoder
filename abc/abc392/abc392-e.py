from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq


class UnionFind():
    """

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        木のサイズを計算

        Parameters
        ---------------------
        x : int
            計算したい木のノード

        Returns
        ---------------------
        size : int
            木のサイズ
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        根のノードを取得

        Returns
        ---------------------
        roots : list
            根のノード
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        グループ数を取得

        Returns
        ---------------------
        size : int
            グループ数
        """
        return len(self.roots())

    def group_members(self):
        """
        全てのグループごとのノードを取得

        Returns
        ---------------------
        group_members : defaultdict
            根をキーとしたノードのリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members



# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

#確認
union=UnionFind(n)




cable=[]
remain=defaultdict(set)
for i in range(m):
    a=list(map(int,input().split()))
    if union.same(a[0]-1,a[1]-1):
        remain[a[0]-1].add((i+1,a[0]-1,a[1]-1))
        remain[a[1]-1].add((i+1,a[0]-1,a[1]-1))
    else:
        union.unite(a[0]-1,a[1]-1)
    # node[a[0]].add(a[1])
    # node[a[1]].add(a[0])


b=union.group_members()


roots=set(b.keys())
print(len(roots)-1)
count=len(roots)
remains=set(remain.keys())



flg=False
while count>1:
    i=roots.pop()
    rem=set()
    for j in b[i]:
        rem|=remain[j]
        del remain[j]
    while rem:
        j=rem.pop()
        other_root=roots.pop()
        for sample in b[other_root]:
            rem|=remain[sample]
            del remain[sample]
        union.unite(other_root,j[1])
        print(j[0],j[1]+1,other_root+1)
        count-=1
        if count==1:
            flg=True
            break
    roots.add(i)
    if flg:
        break

