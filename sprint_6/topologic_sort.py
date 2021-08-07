import sys


class AdjacencyList:
    def __init__(self, size):
        self.vertexes = [None] * (size + 1)
        self.vertexes_num = size

    def add(self, v_from, v_to):
        if self.vertexes[v_from] is None:
            self.vertexes[v_from] = []
        self.vertexes[v_from].append(v_to)

    def get_edges(self, v, reverse=True):
        if self.vertexes[v] is None:
            return []
        edges = self.vertexes[v]
        edges.sort(reverse=reverse)
        return edges

    def get_pow(self, v):
        if self.vertexes[v] is None:
            return 0
        else:
            return len(self.vertexes[v])


class TopologicalSorter:
    def __init__(self):
        self.colors = []
        self.white = 1
        self.grey = 2
        self.black = 3
        self.order = []
        self.adj_list = None

    def sort(self, adj_list: AdjacencyList):
        vertexes = adj_list.vertexes_num + 1
        self.colors = [self.white] * vertexes
        self.adj_list = adj_list
        self.order = []

        for v in range(1, vertexes):
            if self.colors[v] == self.white:
                self.enter_vertex(v)

        self.order.reverse()
        return self.order

    def enter_vertex(self, v):
        self.colors[v] = self.grey
        for w in self.adj_list.get_edges(v):
            if self.colors[w] == self.white:
                self.enter_vertex(w)
        self.colors[v] = self.black
        self.order.append(v)


def main():
    info = sys.stdin.readline().strip().split(' ')
    vertex_num = int(info[0])
    edges_num = int(info[1])

    adj_list = AdjacencyList(vertex_num)

    for i in range(edges_num):
        vertex_pair = sys.stdin.readline().strip().split(' ')

        vertex_from = int(vertex_pair[0])
        vertex_to = int(vertex_pair[1])

        adj_list.add(vertex_from, vertex_to)

    sorter = TopologicalSorter()
    order = sorter.sort(adj_list)

    print(' '.join(map(str, order)))


if __name__ == '__main__':
    main()