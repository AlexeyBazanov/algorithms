import sys


class AdjacencyList:
    def __init__(self, size):
        self.vertexes = [None] * (size + 1)
        self.vertexes_num = size + 1

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


class AdjListBuilder:
    @staticmethod
    def build(is_directed=True):
        info = sys.stdin.readline().strip().split(' ')
        vertex_num = int(info[0])
        edges_num = int(info[1])

        adj_list = AdjacencyList(vertex_num)

        for i in range(edges_num):
            vertex_pair = sys.stdin.readline().strip().split(' ')

            vertex_from = int(vertex_pair[0])
            vertex_to = int(vertex_pair[1])

            adj_list.add(vertex_from, vertex_to)

            if not is_directed:
                adj_list.add(vertex_to, vertex_from)

        return adj_list


class ConnComponentsCounter:
    def __init__(self, start_color=-1):
        self.start_color = start_color
        self.colors = []
        self.counter = 1
        self.adj_list = None

    def count(self, adj_list: AdjacencyList):
        self.adj_list = adj_list
        self.colors = [self.start_color] * adj_list.vertexes_num

        for i in range(1, adj_list.vertexes_num):
            if self.colors[i] == self.start_color:
                self.enter_vertex(i)
                self.counter += 1

        components_count = 1
        components = [[]]

        for i in range(1, adj_list.vertexes_num):
            if len(components) < self.colors[i]:
                components.append([])
                components_count += 1
            components[self.colors[i]-1].append(i)

        return components_count, components

    def enter_vertex(self, v):
        self.colors[v] = self.counter
        for w in self.adj_list.get_edges(v):
            if self.colors[w] == self.start_color:
                self.enter_vertex(w)


def main():
    adj_list = AdjListBuilder.build(is_directed=False)
    counter = ConnComponentsCounter()
    components_count, components = counter.count(adj_list)

    print(components_count)

    for c in components:
        print(' '.join(map(str, c)))


if __name__ == '__main__':
    main()
