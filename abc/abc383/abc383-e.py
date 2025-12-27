from collections import defaultdict,deque
from sortedcontainers import SortedList
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m,k=map(int,input().split())
# s=list(input())
# grid=[list(input()) for _ in range(h)]

num_edges=list()
for i in range(m):
    u,v,w=map(int,input().split())
    num_edges.append((u,v,w))

a=list(map(int,input().split()))
dicta=defaultdict(int)
for i in a:
    dicta[i]+=1
b=list(map(int,input().split()))
dictb=defaultdict(int)
for i in b:
    dictb[i]+=1
num_edges.sort(key=lambda x:x[2])

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

#確認
unio_n=UnionFind(n+1)

ans=0
for i in num_edges:
    unio_n.unite(i[0],i[1])
    if i[0] in dictb:
        p=set(dicta.keys())
        for j in p:
            if unio_n.same(i[0],j):
                while dictb[i[0]] and dicta[j]:
                    ans+=i[2]
                    dictb[i[0]]-=1
                    dicta[j]-=1
                    if dicta[j]==0:
                        del dicta[j]
                    if dictb[i[0]]==0:
                        del dictb[i[0]]
    else:
        p=set(dictb.keys())
        for j in p:
            if unio_n.same(i[0],j):
                while dicta[i[0]] and dictb[j]:
                    ans+=i[2]
                    dicta[i[0]]-=1
                    dictb[j]-=1
                    if dictb[j]==0:
                        del dictb[j]
                    if dicta[i[0]]==0:
                        del dicta[i[0]]
    if i[1] in dictb:
        q=set(dicta.keys())
        for j in q:
            if unio_n.same(i[1],j):
                while dictb[i[1]] and dicta[j]:
                    ans+=i[2]
                    dictb[i[1]]-=1
                    dicta[j]-=1
                    if dicta[j]==0:
                        del dicta[j]
                    if dictb[i[1]]==0:
                        del dictb[i[1]]
    else:
        q=set(dictb.keys())
        for j in q:
            if unio_n.same(i[1],j):
                while dicta[i[1]] and dictb[j]:
                    ans+=i[2]
                    dicta[i[1]]-=1
                    dictb[j]-=1
                    if dictb[j]==0:
                        del dictb[j]
                    if dicta[i[1]]==0:
                        del dicta[i[1]]
print(ans)