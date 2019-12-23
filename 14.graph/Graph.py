import collections
'''
邻接表实现无向图
0 —— 1 —— 2
|    |    |
3 —— 4 —— 5
     |    |
     6 —— 7
'''
class Graph(object):
    def __init__(self, v):
        self.v = v # 顶点个数
        self.adj = [] # 邻接表
        self.found = False
        for _ in range(v):
            self.adj.append([])

    def addEdge(self, s, t):
        self.adj[s].append(t)
        self.adj[t].append(s)

    def bfs(self, s, t):
        '''广度优先搜索'''
        if s == t:
            return

        # 记录已访问的顶点
        visited = [0] * self.v
        # 记录访问路径
        prev = [-1] * self.v
        # 借助队列访问顶点
        queue = [s]
        visited[s] = 1
        
        while queue:
            w = queue.pop(0)
            for i in self.adj[w]:
                if not visited[i]:
                    prev[i] = w
                    if i == t:
                        # self.showPath(s, t, prev)
                        self.showPathRecur(s, t, prev)
                        return
                    visited[i] = 1
                    queue.append(i)

    def dfs(self, s, t):
        '''深度优先搜索'''
        if s == t:
            return
        visited = [0] * self.v
        prev = [-1] * self.v
        self.dfsRecur(s, t, visited, prev)
        self.showPathRecur(s, t, prev)
    
    def dfsRecur(self, s, t, visited, prev):
        if s == t:
            self.found = True
            return

        for i in self.adj[s]:
            if not visited[i]:
                visited[i] = 1
                prev[i] = s
                self.dfsRecur(i, t, visited, prev)
                if self.found:
                    return

    def showPath(self, s, t, prev):
        path = [t]
        if s != t:
            p = prev[t]
            while True:
                path.insert(0, p)
                if p == s:
                    break
                p = prev[p]
        
        for i in path:
            if i == path[-1]:
                print(i)
            else:
                print(i, end="->")
    
    def showPathRecur(self, s, t, prev):
        if s!=t:
            self.showPathRecur(s, prev[t], prev)
        print(t, end=" ")


if __name__ == '__main__':
    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 7)
    g.addEdge(6, 7)
    g.bfs(0,7)
    g.dfs(0, 5)
    # 寻找3度好友（两顶点间有三条边传递）
