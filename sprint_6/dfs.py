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

class DFS:
    def __init__(self):
        self.white = 0
        self.gray = 1
        self.black = 2
        self.colors = []
        self.entry = []
        self.leave = []
        self.time = 0
        self.adj_list = None
        self.callback = None

    def bypass(self, adj_list: AdjacencyList, start_vertex: int, callback=None):
        self.adj_list = adj_list
        self.callback = callback

        self.colors = [self.white] * (adj_list.vertexes_num + 1)

        self.entry = [None] * (adj_list.vertexes_num + 1)
        self.leave = [None] * (adj_list.vertexes_num + 1)
        self.time = 0

        self.enter_vertex(start_vertex)

        for vertex in range(1, adj_list.vertexes_num):
            if self.colors[vertex] == self.white:
                self.enter_vertex(vertex)

        return self.colors, self.entry, self.leave

    def enter_vertex(self, v):
        self.entry[v] = self.time
        self.time += 1
        self.colors[v] = self.gray

        if self.callback:
            self.callback(v)

        for w in self.adj_list.get_edges(v):
            if self.colors[w] == self.white:
                self.enter_vertex(w)

        self.leave[v] = self.time
        self.time += 1
        self.colors[v] = self.black


def add_to_adj_list(adj_list, v_from, v_to):
    if adj_list[v_from] is None:
        adj_list[v_from] = []
    adj_list[v_from].append(v_to)


def create_adj_list(size):
    return [None] * (size + 1)


def get_vertex_pow(adj_list, v):
    if adj_list[v] is None:
        return 0
    else:
        return len(adj_list[v])


def get_vertex_edges(adj_list, v):
    if adj_list[v] is None:
        return []
    edges = adj_list[v]
    edges.sort(reverse=True)
    return edges


def dfs(vertex_list, start_vertex, vertex_num, callback):
    black = 2
    gray = 1
    white = 0
    colors = [white] * (vertex_num + 1)

    stack = [start_vertex]

    while len(stack) > 0:
        v = stack.pop()
        if colors[v] == white:
            colors[v] = gray
            stack.append(v)
            callback(v)
            for w in get_vertex_edges(vertex_list, v):
                if colors[w] == white:
                    stack.append(w)
        elif colors[v] == gray:
            colors[v] = black


output = []


def add_vertex_to_output(v):
    output.append(v)


def main():
    info = sys.stdin.readline().strip().split(' ')
    vertex_num = int(info[0])
    edges_num = int(info[1])

    adj_list = create_adj_list(vertex_num)

    for i in range(edges_num):
        vertex_pair = sys.stdin.readline().strip().split(' ')

        vertex_from = int(vertex_pair[0])
        vertex_to = int(vertex_pair[1])

        add_to_adj_list(adj_list, vertex_from, vertex_to)
        add_to_adj_list(adj_list, vertex_to, vertex_from)

    start_vertex = int(sys.stdin.readline().strip())

    dfs(adj_list, start_vertex, vertex_num, add_vertex_to_output)

    print(' '.join(map(str, output)))


if __name__ == '__main__':
    main()