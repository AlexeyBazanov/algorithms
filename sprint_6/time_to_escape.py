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


def dfs(adj_list: AdjacencyList, start_vertex: int, callback=None):
    black = 2
    gray = 1
    white = 0
    colors = [white] * (adj_list.vertexes_num + 1)

    entry = [None] * (adj_list.vertexes_num + 1)
    leave = [None] * (adj_list.vertexes_num + 1)
    time = 0

    stack = [start_vertex]

    while len(stack) > 0:
        v = stack.pop()
        if colors[v] == white:
            colors[v] = gray
            stack.append(v)

            entry[v] = time
            time += 1

            if callback:
                callback(v)

            for w in adj_list.get_edges(v):
                if colors[w] == white:
                    stack.append(w)
        elif colors[v] == gray:
            colors[v] = black
            leave[v] = time
            time += 1

    return entry, leave


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

    entry, leave = dfs(adj_list, 1)

    for i in range(1, vertex_num+1):
        print('{0} {1}'.format(entry[i], leave[i]))


if __name__ == '__main__':
    main()
