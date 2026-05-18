import csv
from collections import deque

class FlowCalculator:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, capacity):
        if u not in self.graph: self.graph[u] = {}
        if v not in self.graph: self.graph[v] = {}
        self.graph[u][v] = self.graph[u].get(v, 0) + capacity
        if u not in self.graph[v]: self.graph[v][u] = 0

    def bfs(self, source, sink, parent):
        visited = {node: False for node in self.graph}
        queue = deque([source])
        visited[source] = True
        while queue:
            u = queue.popleft()
            for v, cap in self.graph[u].items():
                if not visited.get(v, False) and cap > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink: return True
        return False

    def max_flow(self, source, sink):
        parent = {}
        max_f = 0
        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_f += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_f

def solve_flower_delivery(file_path):
    calc = FlowCalculator()
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
        farms = [x.strip() for x in lines[0].split(',')]
        shops = [x.strip() for x in lines[1].split(',')]
        s_src, s_snk = "SOURCE", "SINK"
        for farm in farms: calc.add_edge(s_src, farm, float('inf'))
        for shop in shops: calc.add_edge(shop, s_snk, float('inf'))
        for line in lines[2:]:
            p = [i.strip() for i in line.split(',')]
            if len(p) == 3: calc.add_edge(p[0], p[1], int(p[2]))
        return calc.max_flow(s_src, s_snk)
    except: return 0

if __name__ == "__main__":
    print(f"Результат: {solve_flower_delivery('roads.csv')}")
