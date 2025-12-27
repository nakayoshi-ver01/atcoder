from collections import defaultdict
import heapq

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


n,m=map(int,input().split())
grid=[list(input()) for _ in range(n)]

cells_log_of_reach_cells = [[10**4 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j]!='#':
            reach_cells=1
            for k in reversed(range(i)):
                if grid[k][j]=='.':
                    reach_cells+=1
                else:
                    break
            for k in range(i+1,n):
                if grid[k][j]=='.':
                    reach_cells+=1
                else:
                    break
            for k in reversed(range(j)):
                if grid[i][k]=='.':
                    reach_cells+=1
                else:
                    break
            for k in range(j+1,n):
                if grid[i][k]=='.':
                    reach_cells+=1
                else:
                    break
            cells_log_of_reach_cells[i][j]=reach_cells
#確認
a=UnionFind(n**2)
directorys=[(0,1),(1,0),(-1,0),(0,-1)]
for i in range(n):
    for j in range(n):
        if grid[i][j]=='#':
            a.unite(i*n+j,n*n)
        else:
            for directory_i,directory_j in directorys:
                next_point=(i+directory_i,j+directory_j)
                if 0<=next_point[0]<=n-1 and 0<=next_point[1]<=n-1:
                    if grid[next_point[0]][next_point[1]]=='.':
                        a.unite(next_point[0]*n+next_point[1],i*n+j)

readers=a.roots()
y=a.group_members()
dict_to_list =list()
for i in readers:
    dict_to_list.append(y[i])

dict_to_list.sort(key=lambda x:len(x))

for cells in dict_to_list:
    if grid[cells[0]//n][cells[0]%n]=='.':
        cells_order_by_reach_cells=list()
        for cell in cells:
            heapq.heappush(
                cells_order_by_reach_cells,
                (cells_log_of_reach_cells[cell//n][cell%n],(cell//n,cell%n))
            )
        while cells_order_by_reach_cells:
            next_cell=heapq.heappop(cells_order_by_reach_cells)
            print(*next_cell[1])