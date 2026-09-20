#深さ優先(ルート数)
from collections import defaultdict
import sys
sys.setrecursionlimit(1000010)
def dfs(s,i,afnode):
    afnode.add(i)
    for d in s[i]:
        if d not in afnode:
            count+=1
            dfs(s,d,afnode)
    afnode.remove(i)
    return count
    
    
s=defaultdict(set)
 
flag=0
n,m=map(int,input().split())
for i in range(m):
    a,b=map(int,input().split())
    s[a].add(b)
    s[b].add(a)

root=set()
afnode=set()
z=1
ssss=dfs(s,z,afnode)
print(ssss)


#連結成分取得(Union-findでもいい気が…)
from collections import defaultdict
aaa=defaultdict(set)
n,m=map(int,input().split())
node=set(i+1 for i in range(n))
for i in range(m):
    a,b=map(int,input().split())
    aaa[a].add(b)
    aaa[b].add(a)
count=0
while len(node)>0:
    s=node.pop()
    b={s}
    while len(b)>0:
        k=b.pop()
        for i in range(len(aaa[k])):
            c=aaa[k].pop()
            if c in node:
                b.add(c)
        node-=b
    count+=1
print(count)


#高速素因数分解(素数列挙+素因数分解)
def eratosthenes(n):
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if not(is_prime[p]):
            continue
        for k in range(p*2, n+1, p):
            is_prime[k] = False
    return is_prime

k=eratosthenes(10**7+1)
prime_numbers=[]
for i in range(10**7+1):
    if k[i]:
        prime_numbers.append(i)

def factorization(n):
    global prime_numbers
    arr = []
    temp = n
    for i in prime_numbers:
        if i**2>n:
            break
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

#nまでの素数判定
def prime_judge(n):
    num={i for i in range(2,n+1)}
    for i in range(2,int(n**(1/2))+1):
        if i in num:
            for j in range(2,n//i+1):
                if i*j in num:
                    num.remove(i*j)
                if i*j>n:
                    break
    return list(num)


#アルファベット辞書
komoji=[chr(i) for i in range(97,123)]
omoji=[chr(i) for i in range(65,91)]

#入力読み出し
n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
s=list(input())


#階乗
def factorial(n):
    k=1
    for i in range(1,n+1):
        k*=i
    return k

#unionfind木(提出時はpypyじゃないほうがよさそう)
from collections import defaultdict

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
        group_members = defaultdict(set)
        for member in range(self.n):
            group_members[self.find(member)].add(member)
        return group_members

#確認
a=UnionFind(6)
b=a.group_members()
print(b)

#二分探索木
class Node:#ノードを定義
    def __init__(self, data): #コンストラクタ
        self.data = data #ノードがもつ数値
        self.left = None #左エッジ
        self.right = None #右エッジ

class BST:#木を定義(+ノード追加機能)
    def __init__(self,datalist):
        self.root = None #ルート初期化
        for node in datalist: #数値を持つ配列から二分木を生成
            self.insert(node) #挿入メソッドを使ってノードを挿入する
    
    def insert(self,data):
        n=self.root
        if self.root is None:
            self.root=Node(data)
            return
        else:
            while True: #return等が入るまでずっと実行
                entry = n.data #entryにnが持つデータ(数値)を入れる
                if data < entry: #entryとdata(代入するデータ)を比較してentryの方が大きい場合
                    if n.left is None: #nの左エッジに何も入っていない場合
                        n.left = Node(data) #nの左エッジにdata(代入するデータ)を代入
                        return ##呼び出し部分に戻る
                    n = n.left #nの左に何か入っている場合nにnのleftを代入
                elif data > entry: #entryとdata(代入するデータ)を比較してentryの方が小さい場合
                    if n.right is None: #nの右エッジに何も入っていない場合
                        n.right = Node(data) #nの右エッジにdata(代入するデータ)を代入
                        return #呼び出し部分に戻る
                    n = n.right #nの右エッジに何か入っている場合nにnのrightを代入
                else: #上2つの条件分岐以外の場合
                    n.data = data #nのdataにdata(代入するデータ)を代入
                    return #呼び出し部分に戻る
    
    
def preorder(node):#通過順に出力
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def inorder(node):#数値の昇順に出力
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)          

def postorder(node):#左ノードから深い順に出力
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

def width(n,node):#n:ノード総数,浅い順に左ノードから出力
    search=list(node)
    for i in range(0,n):
        if node.left.data:
            search.append(node.left)
        if node.right.data:
            search.append(node.right)

    for i in range(0,n):
	    print(search[i].data) 

   
addlist=list(map(int,input().split()))
tree=BST(addlist)
preorder(tree.root)

def modeq(b,a,p):#一次合同式(分子,b:分母,a)
    z=b*pow(a,p-2,p)
    z%=p
    return z

#二分探索
left=0
right=len(a)
while 1:
    center=(left+right)//2
    if a[center]==n:
        print(center+1,a[center])
        break
    elif a[center]>n:
        right=center-1
        print(center+1,a[center])
    elif a[center]<n:
        left=center+1
        print(center+1,a[center])
    if left>=right:
        print(-1)
        break

#bit全探索
rr={i for i in range(10)}
for i in rr:
    li=list(i)
    bit=[0 for i in range(len(li))]
    for j in range(1,2**len(i)-1):
        bitcheck=j
        for k in range(len(bit)):
            bit[len(bit)-k-1]=bitcheck%2
            bitcheck//=2

        test=set()
        for k,b in zip(li,bit):
            if b==1:
                test.add(k)
n=int(input())
for i in range(2**n):
    k=i
    cur=0
    popbit=set()
    while k>0:
        if k%2==1:
            popbit.add(cur)
        cur+=1
        k//=2
    print(popbit)
    
#優先度付きキュー
import heapq
x=list()
v=list(map(int,input().split()))
for i in range(10):
    heapq.heappush(x,v[i])#xにiを追加
    print(x)
for i in range(10):
    least=heapq.heappop(x)#xから最小要素取得
    print(least,x)

#平衡二分木

class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1<<n, 1<<n)

    def append(self, v):# v を追加（その時点で v はない前提）
        v += 1
        nd = self.root
        while True:
            if v == nd.value:
                # v がすでに存在する場合に何か処理が必要ならここに書く
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p&-p)//2)
                        break

    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd

    def find_l(self, v): # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v): # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1<<self.N)-1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd = None, prev = None): # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        if not nd: nd = self.root
        if not prev: prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    #####
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    #####
                    return
        if (not nd.left) and (not nd.right):
            if not prev.left:
                prev.right = None
            elif not prev.right:
                prev.left = None
            else:
                if nd.pivot == prev.left.pivot:
                    prev.left = None
                else:
                    prev.right = None

        elif nd.right:
            # print("type A", v)
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)    
        else:
            # print("type B", v)
            nd.value = self.rightmost(nd.left).value
            self.delete(nd.value - 1, nd.left, nd)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None

    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.pivot - 1, nd_.left.value - 1 if nd_.left else -1, nd_.right.value - 1 if nd_.right else -1)

        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re
        print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])

    def debug_list(self):
        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(nd.value - 1)
            if nd.right:
                re += debug_node(nd.right)
            return re
        return debug_node(self.root)[:-1]

BT = BalancingTree(5) # 2**n-1 までの要素を入れられるピボット木(多分)
BT.append(3)#データの追加
BT.append(20)
BT.append(5)
BT.append(10)
BT.append(13)
BT.append(8)
BT.delete(20)#データの削除
print(BT.find_l(12)) # 10 ()内の次に小さいデータを出力
print(BT.find_r(5)) # 8 ()内の次に大きいデータを出力
print(BT.min) # 3 最小データを出力
print(BT.max) # 13 最大データを出力
print(3 in BT) # True
print(4 in BT) # False
print(BT.debug_list()) # 中身の確認


#繰り返し二乗法
k=10
ten=[1,10]
for i in range(1,k+1):#  a**2**0からa**2**kまでの素数で割った余りを計算
    ten.append((ten[i]**2)%(10**9+7))


import math
a=int(input())
b=int(input())
print(math.gcd(a,b))#最大公約数
print((a*b)//math.gcd(a,b))#最小公倍数


#セグメント木
import sys

def op(x, y):#指定される演算を定義
    return x + y

def e():#演算の単位元を定義(掛け算なら1,足し算なら0など)
    return 0


class SegTree:
    def __init__(self, op, e, n, v=None):#与えられた引数で初期化
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def set(self, p, x):#セグ木に値を入れる
        p += self._size
        self._d[p] = x
        while p > 1:
            p >>= 1
            self._d[p] = self._op(self._d[p << 1], self._d[p << 1 | 1])

    def get(self, p):#セグ木の値を取り出す
        return self._d[p + self._size]

    def prod(self, l, r):#セグ木内の[l,r)の範囲で計算を行う
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

    def all_prod(self):#全体の計算結果を返す
        return self._d[1]

    def check(self):#セグ木全体の中身の確認
        print(self._d)
        return 0
n=16
A=[i for i in range(n)]


seg = SegTree(op, e, n, A)# nはAの長さ, Aはリスト
seg.check()
for i in range(n):
    if i%2==0:
        seg.set((i)%n,seg.get((i)%n)+2)
    else:
        print(seg.prod(i,min(i+2,n-1)))
    seg.check()

#fenwick木(BIT)
class FenwickTree:
    """
    区間和・点更新が O(log n) の Fenwick 木

    Attributes
    --------------------
    n : int
        要素数
    data : list
        内部配列(1-indexed)
    """

    def __init__(self, n, v=None):
        """
        Parameters
        ---------------------
        n : int
            要素数
        v : list, optional
            初期値(0-indexed)。省略時は全て 0
        """
        self.n = n
        self.data = [0] * (n + 1)
        if v is not None:
            for i, x in enumerate(v):
                self.add(i, x)

    def add(self, p, x):
        """
        A[p] に x を加算

        Parameters
        ---------------------
        p : int
            更新位置(0-indexed)
        x : int
            加算する値
        """
        p += 1
        while p <= self.n:
            self.data[p] += x
            p += p & -p

    def set(self, p, x):
        """
        A[p] を x に更新

        Parameters
        ---------------------
        p : int
            更新位置(0-indexed)
        x : int
            代入する値
        """
        self.add(p, x - self.get(p))

    def get(self, p):
        """
        A[p] を取得

        Parameters
        ---------------------
        p : int
            取得位置(0-indexed)

        Returns
        ---------------------
        ans : int
            A[p] の値
        """
        return self.prod(p, p + 1)

    def _sum(self, r):
        """[0, r) の和"""
        s = 0
        while r > 0:
            s += self.data[r]
            r -= r & -r
        return s

    def prod(self, l, r):
        """
        [l, r) の区間和

        Parameters
        ---------------------
        l : int
            左端(含む, 0-indexed)
        r : int
            右端(含まない, 0-indexed)

        Returns
        ---------------------
        ans : int
            区間和
        """
        return self._sum(r) - self._sum(l)

    def all_prod(self):
        """全体の和"""
        return self._sum(self.n)

#確認(転倒数カウント)
# n = int(input())
# A = list(map(int, input().split()))
# bit = FenwickTree(n)
# inv = 0
# for val, idx in sorted((A[i], i) for i in range(n)):
#     inv += bit.prod(idx + 1, n)  # 右側の和
#     bit.add(idx, 1)
# print(inv)

#トポロジカルソート
from collections import defaultdict
import heapq
def topological_sort(n,G, into_num):#ノード数,行先辞書,受入辞書
    # 入ってくる有向辺を持たないノードを列挙
    q = list()
    heapq.heapify(q)
    # V: 頂点数
    for i in range(n):
        if len(into_num[i+1]) == 0:
            heapq.heappush(q,i+1)
    # 以下、幅優先探索
    ans = []
    while q:
        v = heapq.heappop(q)
        ans.append(v)
        for adj in G[v]:
            into_num[adj].remove(v)  # 入次数を減らす
            if len(into_num[adj]) == 0:
                heapq.heappush(q,adj)  # 入次数が0になったら、キューに入れる
        G[v].clear()

    return ans

#幅優先探索
from collections import defaultdict,deque
edge=defaultdict(set)#辺を管理
n,m=map(int,input().split())#ノード数,辺数取得(ここら辺は問題によりけり)
for i in range(m):
    a,b=map(int,input().split())
    edge[a].add(b)
    edge[b].add(a)

search=deque()
search.append(1)
af={1}
while search:#探索場所移動テンプレ
    k=search.popleft()
    for i in edge[k]:
        if i not in af:
            search.append(i)
            af.add(i)
            #ここに探索内容を書く


# 枠ごとに回転
import copy
n=int(input())
# 入力
grid=[list(input()) for _ in range(n)]
# 作業用grid (空配列のほうが良いかも)
def ringrotate(n,m,grid):
    mapping=copy.deepcopy(grid)
    #途中
    # mapping=[['.' for _ in range(n)] for _ in range(n)]
    for j in range(i,n-i):
        mapping[i][n-1-j]=grid[j][i]
    for j in range(i,n-i):
        mapping[n-1-i][n-1-j]=grid[j][n-1-i]
    for k in range(i,n-i):
        mapping[k][n-1-i]=grid[i][k]
    for k in range(i,n-i):
        mapping[k][i]=grid[n-1-i][k]

# 一括回転
import copy
n=int(input())
# 入力
grid=[list(input()) for _ in range(n)]
def rotate(n,grid):
    """
    正方形のlistを回転させる:O(n^2)
    args:
        n:gridの大きさ
        grid:正方行列(list)
    return:
        mapping:90度回転させたgrid
    """
    # 作業用grid (空配列のほうが良いかも)
    mapping=copy.deepcopy(grid)
    # mapping=[['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mapping[j][n-1-i]=grid[i][j]
    return mapping


# ワーシャルフロイド法
n,m=map(int,input().split())
# 経路テーブル
path_length=[[10**20 for _ in range(n+1)] for _ in range(n+1)]
# 同じ場所はもちろん距離0
for i in range(n+1):
    path_length[i][i]=0
# 経路の記録
for i in range(m):
    a,b,l=map(int,input().split())
    path_length[a][b]=l
    path_length[b][a]=l
# kを経由した際のi,j間の距離をそれぞれ計算しなおす
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            path_length[i][j]=min(path_length[i][j],path_length[i][k]+path_length[k][j])


# ダブリング
n,k=map(int,input().split())
# xが移動方法aが実際に動かすもの
x=list(map(int,input().split()))
a=list(map(int,input().split()))

# 0-indexedにする(計算のしやすさ意識) 
for i in range(n):
    x[i]-=1
# ダブリングテーブル作成
doubling=list()
doubling.append(x)

# 2の60乗まで計算
for i in range(61):
    # 計算用リスト
    b=list()
    # ダブリングを(i-1)回行ったものをさらにダブリングする(2**i回操作した時の状態を保存)
    for j in doubling[-1]:
        b.append(doubling[-1][j])
    doubling.append(b)

# 2**cur乗するか記録
cur=0
# 現在の並び順を記録
now=[i for i in range(n)]
while k>0:
    if k%2==1:
        # 計算用にコピー
        tmp=now[::]
        for i in range(n):
            now[i]=tmp[doubling[cur][i]]
    cur+=1
    k//=2
ans=[]
# 最後にaの要素を並び替えて終了
for i in range(n):
    ans.append(a[now[i]])
print(*ans)

# 二次元累積和
n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

cumulative_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        cumulative_sum[i+1][j+1] = cumulative_sum[i+1][j]+a[i][j]


for i in range(n):
    for j in range(m):
        cumulative_sum[i+1][j+1] += cumulative_sum[i][j+1]


for i in range(n+1):
    print(cumulative_sum[i])


# LIS(最長増加部分列)
import bisect
n=int(input())
a = list(map(int,input().split()))
ans=0
length=[10**9 for _ in range(n+1)]
length[0]=0
dp=[0 for _ in range(n+1)]
for i in range(n):
    pos = bisect.bisect_left(length,a[i])
    dp[i] = pos

    length[dp[i]]=a[i]
    if dp[i]>ans:
        ans+=1
print(ans)


# bitdp

n,m=map(int,input().split())
dp=[[10**10 for _ in range(2**n+1)] for _ in range(m+1)]
member=list()
for i in range(m):
    a,*b=map(int,input().split())
    member.append(b)

dp[0][0]=0
for i in range(m):
    for j in range(2**n):
        dp[i+1][j]=min(dp[i+1][j],dp[i][j])
        move=0
        for k in member[i]:
            move+=2**k
        dp[i+1][j|move]=min(dp[i+1][j|move],dp[i][j]+1)
    # print(i,dp[i+1])


# 木dp
from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
# 木作成
edge=defaultdict(int)
for i in range(2,n+1):
    edge[i]=a[i-2]
# dp開始
dp=[0 for i in range(n+1)]
for i in reversed(range(2,n+1)):
    dp[edge[i]]+=dp[i]+1
    print(*dp[1:])



# グラフ上の再帰dp
from collections import defaultdict
from functools import lru_cache
import sys

sys.setrecursionlimit(10**9)
n,m=map(int,input().split())
# 木作成
edge=defaultdict(set)
no_in={i+1 for i in range(n)}
for _ in range(m):
    x,y=map(int,input().split())
    edge[x].add(y)
    no_in.discard(y)

dp=[-1 for _ in range(n+1)]
@lru_cache
def search(n):
    global dp
    global edge
    if dp[n]!=-1:
        return dp[n]
    f=0
    for i in edge[n]:
        f=max(search(i)+1,f)
    dp[n]=f
    return dp[n]

for i in no_in:
    search(i)
print(max(dp))

# グリッドdp

h,w=map(int,input().split())
# a=list(map(int,input().split()))
grid=[list(input()) for _ in range(h)]
mod=10**9+7
pattern=[[0 for _ in range(w)] for _ in range(h)]
pattern[0][0]=1
for i in range(h):
    for j in range(w):
        a=0
        b=0
        if grid[i][j]!='#' and (i,j)!=(0,0):
            if i>0 and grid[i-1][j]=='.':
                a=pattern[i-1][j]
            if j>0 and grid[i][j-1]=='.':
                b=pattern[i][j-1]
            pattern[i][j]=(a+b)%mod


# ちょうどi枚になる確率のdp

n=int(input())
p=list(map(float,input().split()))
dp=[[0 for _ in range(n+1)] for _ in range(n+1)]

dp[0][0]=1

for i in range(1,n+1):
    for j in range(i+1):
        dp[i][j]=dp[i-1][j-1]*p[i-1]+dp[i-1][j]*(1-p[i-1])

print(sum(dp[-1][(n+1)//2:]))


# 期待値dp(一例)
from functools import lru_cache
import sys 
sys.setrecursionlimit(10**8)
n=int(input())
a=list(map(int,input().split()))

dp=[[[0 for _ in range(n+2)] for _ in range(n+2)] for _ in range(n+2)]

# どうやら内側からのほうがよさそう(そうじゃないと誤答になる)
for k in range(n+1):
    for j in range(n+1):
        for i in range(n+1):
            if i+j+k==0:
                continue
            prob=n/(i+j+k)
            if i>0:
                prob+=dp[i-1][j][k]*i/(i+j+k)
            if j>0:
                prob+=dp[i+1][j-1][k]*j/(i+j+k)
            if k>0:
                prob+=dp[i][j+1][k-1]*k/(i+j+k)
            dp[i][j][k]=prob
dishes=[0,0,0,0]
for i in a:
    dishes[i]+=1

print(dp[dishes[1]][dishes[2]][dishes[3]])



#セグ木の演算例
st = SegTree([0]*N,segfunc,0)
st.query(0,4)
"""
操作 segfunc 単位元
最小値 min(x,y) math.inf
最大値 max(x,y) -math.inf
区間和 x+y 0
区間積 x*y 1
最大公約数 math.gcd(x,y) 0
"""

# 遅延セグ木(区間加算)　
def segfunc(x,y):
    return x+y
class LazySegTree_RAQ:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [0]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
    def gindex(self,l,r):
        l += self.num
        r += self.num
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        while r>l:
            if l<=lm:
                yield l
            if r<=rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1
    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v==0:
                continue
            self.lazy[i] = 0
            self.lazy[2*i] += v
            self.lazy[2*i+1] += v
            self.tree[2*i] += v
            self.tree[2*i+1] += v
    def add(self,l,r,x):
        ids = self.gindex(l,r)
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] += x
                self.tree[l] += x
                l += 1
            if r&1:
                self.lazy[r-1] += x
                self.tree[r-1] += x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1]) + self.lazy[i]
    def query(self,l,r):
        self.propagates(*self.gindex(l,r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res

# 畳み込み？
import numpy as np

n,m=map(int,input().split()) 
a=list(map(int,input().split()))
a.sort()
b=[0 for _ in range(a[-1]+1)]
for i in a:
    b[i]+=1

c=list(map(int,input().split()))
c.sort()
d=[0 for _ in range(c[-1]+1)]
for i in c:
    d[i]+=1

f = np.array(b)
g = np.array(d)
fft_len = 1  # |f|+|g|-1 以上の2の冪数
while fft_len<len(f)+len(g)-1:
    fft_len*=2


# f,gをフーリエ変換
Ff = np.fft.rfft(f, fft_len)
print(Ff)
Fg = np.fft.rfft(g, fft_len)
print(Fg)
 
# 各要素について掛け合わせる
Ffg = Ff * Fg
print(Ffg)
 
# 逆変換後、整数に丸める
fg = np.fft.irfft(Ffg, fft_len)
fg = np.rint(fg)
print(fg)


# エラトステネスの篩
def eratosthenes(n):
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if not(is_prime[p]):
            continue
        for k in range(p*2, n+1, p):
            is_prime[k] = False
    return is_prime

# 分割

n,m=map(int,input().split())
w=list(map(int,input().split()))
c=list(map(int,input().split()))

w.sort(reverse=True)
c.sort(reverse=True)
def split(trucks,i):
    '''
    Docstring for split
    
    :param trucks: 状態
    :param i: 追加対象

    w,c: リスト
    n,m: w,cのリスト長
    '''
    global w
    global c
    global n
    global m
    ans='No'
    if i==n:
        return 'Yes'
    
    for j in range(len(trucks)):
        if trucks[j]+w[i]<=c[j]:
            # 追加→再帰→元の状態に戻す
            trucks[j]+=w[i]
            ans=split(trucks,i+1)
            trucks[j]-=w[i]
        if ans=='Yes':
            # okパターンが見つかったら即終了
            return ans
    
    if len(trucks)<m and w[i]<=c[j+1]:
        # 追加→再帰→元の状態に戻す
        trucks.append(w[i])
        ans=split(trucks,i+1)
        del trucks[-1]
        if ans=='Yes':
            # okパターンが見つかったら即終了
            return ans
    else:
        # 途中で追加できなくなったらそれ以降も追加できない
        return 'No'
    
    return ans


# コンビネーションやり方2選
# 1.すべて階乗を用いる方法

MOD=998244353

kaijo_log=[1]
for i in range(1,n+1):
    kaijo_log.append((kaijo_log[-1]*i)%MOD)

def combination(n,r):
    # 事前計算でn!,n-r!,r!を用意しておいて、nCrを計算する,(n,rともに一定の範囲内で何度も計算する場合に有効)
    return (kaijo_log[n]*pow(kaijo_log[r],MOD-2,MOD)*pow(kaijo_log[n-r],MOD-2,MOD))%MOD


# 2.分子だけ階乗を用いる方法

def kaijomod(gl,num):
    '''
    gl:かける最大の数,num:かける個数
    gl=5,num=3なら5*4*3
    '''
    ans=1
    for i in range(num):
        ans*=gl-i
        ans%=MOD
    return ans

def combination_2(n,r):
    # nPrを実際に計算してからr!で割る(nが巨大かつrが小さい場合に有効)
    return (kaijomod(n,r)*pow(kaijo_log[r],MOD-2,MOD))%MOD


# Floor Sum
def floor_sum(n, m, a, b):
    """
    sum(floor((a*i+b)/m) for i in range(n)) を O(log(max(a, m))) で求める。

    n >= 0, m >= 1
    a, b は負でもよい。
    """
    assert n >= 0 and m >= 1

    # a, b を 0 <= a, b < m に正規化し、商の寄与を先に加える
    qa, a = divmod(a, m)
    qb, b = divmod(b, m)
    ans = qa * n * (n - 1) // 2 + qb * n

    while True:
        # a, b が m 以上なら、その整数部分を答えに加える
        if a >= m:
            ans += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m

        y_max = a * n + b
        if y_max < m:
            return ans

        # 格子点の数え上げで x 軸と y 軸を入れ替える
        n, b = divmod(y_max, m)
        m, a = a, m


# Trie木
class Trie:
    """
    文字列の挿入・検索・接頭辞カウントが O(|S|) の Trie 木

    Attributes
    --------------------
    root : Node
        根ノード
    """

    class Node:
        def __init__(self):
            self.child = {}
            self.cnt = 0  # このノードを通る文字列の個数
            self.end = 0  # このノードで終わる文字列の個数

    def __init__(self):
        self.root = self.Node()

    def insert(self, s):
        """
        文字列 s を挿入

        Parameters
        ---------------------
        s : str
            挿入する文字列
        """
        nd = self.root
        nd.cnt += 1
        for c in s:
            if c not in nd.child:
                nd.child[c] = self.Node()
            nd = nd.child[c]
            nd.cnt += 1
        nd.end += 1

    def delete(self, s):
        """
        文字列 s を 1 つ削除(存在しなければ何もしない)

        Parameters
        ---------------------
        s : str
            削除する文字列

        Returns
        ---------------------
        ans : bool
            削除できたか
        """
        if self.count(s) == 0:
            return False
        nd = self.root
        nd.cnt -= 1
        for c in s:
            nd = nd.child[c]
            nd.cnt -= 1
        nd.end -= 1
        return True

    def _walk(self, s):
        nd = self.root
        for c in s:
            if c not in nd.child:
                return None
            nd = nd.child[c]
        return nd

    def count(self, s):
        """
        文字列 s と完全一致する個数

        Parameters
        ---------------------
        s : str
            検索する文字列

        Returns
        ---------------------
        ans : int
            完全一致する個数
        """
        nd = self._walk(s)
        return 0 if nd is None else nd.end

    def count_prefix(self, s):
        """
        接頭辞が s である文字列の個数

        Parameters
        ---------------------
        s : str
            接頭辞

        Returns
        ---------------------
        ans : int
            接頭辞が s である個数
        """
        nd = self._walk(s)
        return 0 if nd is None else nd.cnt

    def search(self, s):
        """
        文字列 s が存在するか判定

        Parameters
        ---------------------
        s : str
            検索する文字列

        Returns
        ---------------------
        ans : bool
            存在するか
        """
        return self.count(s) > 0

    def starts_with(self, s):
        """
        接頭辞 s を持つ文字列が存在するか判定

        Parameters
        ---------------------
        s : str
            接頭辞

        Returns
        ---------------------
        ans : bool
            存在するか
        """
        return self.count_prefix(s) > 0

    def __contains__(self, s):
        return self.search(s)

    def __len__(self):
        return self.root.cnt

#確認
# trie = Trie()
# trie.insert("abc")
# trie.insert("abd")
# trie.insert("abc")
# print(trie.search("abc"))        # True
# print(trie.count("abc"))         # 2
# print(trie.count_prefix("ab"))   # 3
# print(trie.starts_with("ac"))    # False
# trie.delete("abc")
# print(trie.count("abc"))         # 1
# print("abc" in trie)             # True
# print(len(trie))                 # 2


# Binary Trie(XOR用)
class BinaryTrie:
    """
    非負整数の挿入・削除・XOR最大/最小が O(bit) の Binary Trie

    Attributes
    --------------------
    bit : int
        扱うビット長(32 なら [0, 2^32)、60 なら 10^18 まで)
    child : list
        各ノードの子 [0側, 1側] (無い場合は -1)
    cnt : list
        各ノードを通る整数の個数
    """

    def __init__(self, bit_length=32):
        """
        Parameters
        ---------------------
        bit_length : int
            扱うビット長。A_i < 2^30 なら 30、10^18 なら 60
        """
        self.bit = bit_length
        self.child = [[-1, -1]]
        self.cnt = [0]

    def _new_node(self):
        self.child.append([-1, -1])
        self.cnt.append(0)
        return len(self.child) - 1

    def insert(self, x, count=1):
        """
        整数 x を count 個挿入

        Parameters
        ---------------------
        x : int
            挿入する非負整数
        count : int
            挿入する個数
        """
        v = 0
        self.cnt[v] += count
        for i in range(self.bit - 1, -1, -1):
            b = (x >> i) & 1
            if self.child[v][b] == -1:
                self.child[v][b] = self._new_node()
            v = self.child[v][b]
            self.cnt[v] += count

    def delete(self, x, count=1):
        """
        整数 x を count 個削除(存在しなければ何もしない)

        Parameters
        ---------------------
        x : int
            削除する非負整数
        count : int
            削除する個数

        Returns
        ---------------------
        ans : bool
            削除できたか
        """
        if self.count(x) < count:
            return False
        v = 0
        self.cnt[v] -= count
        for i in range(self.bit - 1, -1, -1):
            b = (x >> i) & 1
            v = self.child[v][b]
            self.cnt[v] -= count
        return True

    def count(self, x):
        """
        整数 x の個数

        Parameters
        ---------------------
        x : int
            検索する非負整数

        Returns
        ---------------------
        ans : int
            x の個数
        """
        v = 0
        for i in range(self.bit - 1, -1, -1):
            b = (x >> i) & 1
            if self.child[v][b] == -1:
                return 0
            v = self.child[v][b]
        return self.cnt[v]

    def xor_max(self, x):
        """
        集合内の y について x XOR y の最大値を返す(空なら None)

        Parameters
        ---------------------
        x : int
            XOR する値

        Returns
        ---------------------
        ans : int or None
            最大の XOR 値
        """
        if self.cnt[0] == 0:
            return None
        v = 0
        ans = 0
        for i in range(self.bit - 1, -1, -1):
            b = (x >> i) & 1
            want = b ^ 1
            nxt = self.child[v][want]
            if nxt != -1 and self.cnt[nxt] > 0:
                ans |= 1 << i
                v = nxt
            else:
                v = self.child[v][b]
        return ans

    def xor_min(self, x):
        """
        集合内の y について x XOR y の最小値を返す(空なら None)

        Parameters
        ---------------------
        x : int
            XOR する値

        Returns
        ---------------------
        ans : int or None
            最小の XOR 値
        """
        if self.cnt[0] == 0:
            return None
        v = 0
        ans = 0
        for i in range(self.bit - 1, -1, -1):
            b = (x >> i) & 1
            nxt = self.child[v][b]
            if nxt != -1 and self.cnt[nxt] > 0:
                v = nxt
            else:
                ans |= 1 << i
                v = self.child[v][b ^ 1]
        return ans

    def kth(self, k):
        """
        小さい方から k 番目(0-indexed)の値を返す

        Parameters
        ---------------------
        k : int
            順位(0-indexed)

        Returns
        ---------------------
        ans : int or None
            k 番目の値。範囲外なら None
        """
        if k < 0 or k >= self.cnt[0]:
            return None
        v = 0
        ans = 0
        for i in range(self.bit - 1, -1, -1):
            left = self.child[v][0]
            left_cnt = self.cnt[left] if left != -1 else 0
            if k < left_cnt:
                v = left
            else:
                k -= left_cnt
                ans |= 1 << i
                v = self.child[v][1]
        return ans

    def __len__(self):
        return self.cnt[0]

    def __contains__(self, x):
        return self.count(x) > 0

#確認
# bt = BinaryTrie(4)  # [0, 16) まで
# bt.insert(3)
# bt.insert(5)
# bt.insert(10)
# print(bt.xor_max(6))   # 12 (6 XOR 10)
# print(bt.xor_min(6))   # 1  (6 XOR 5)
# print(bt.kth(0))       # 3
# print(bt.kth(2))       # 10
# bt.delete(5)
# print(5 in bt)         # False
# print(len(bt))         # 2