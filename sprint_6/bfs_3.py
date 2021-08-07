from collections import defaultdict
import sys


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def get_edges(self, u):
        self.graph[u].sort()
        return self.graph[u]

    def vertexes_num(self):
        if len(self.graph) > 0:
            return max(self.graph)
        else:
            return 1

    def BFS(self, s):
        visited = [False] * (self.vertexes_num() + 1)
        queue = [s]
        visited[s] = True
        order = []

        while queue:
            s = queue.pop(0)
            order.append(s)

            for i in self.get_edges(s):
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

        return order


def main():
    info = sys.stdin.readline().strip().split(' ')
    edges_num = int(info[1])
    graph = Graph()

    for i in range(edges_num):
        vertex_pair = sys.stdin.readline().strip().split(' ')
        u = int(vertex_pair[0])
        v = int(vertex_pair[1])
        graph.add_edge(u, v)
        graph.add_edge(v, u)

    start_vertex = int(sys.stdin.readline().strip())
    order = graph.BFS(start_vertex)
    print(' '.join(map(str, order)))


if __name__ == '__main__':
    main()
