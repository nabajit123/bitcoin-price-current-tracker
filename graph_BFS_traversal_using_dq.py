from collections import defaultdict, deque
from dataclasses import dataclass, asdict

# container deque -> both append and pop operation take o(1)
# unlike implement queue using list take o(n) time

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, a, b):
        self.graph[a].append(b)
        
    def BFS(self, s):
        
        visited = [False]* (max(self.graph)+1)
        
        queue = deque()
        queue.append(s)
        visited[s] = True
        while queue:
             s = queue.popleft()
             print(s)
             for i in self.graph[s]:
                 if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                                
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.__dict__)
g.BFS(2)