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


class GraphCrawler:
    @staticmethod
    def bfs(adj_list: AdjacencyList, start_vertex: int, enter_callback=None, leave_callback=None):
        white = 0
        gray = 1
        black = 2
        colors = [white] * adj_list.vertexes_num
        colors[start_vertex] = gray

        planned = [start_vertex]
        distances = [-1] * adj_list.vertexes_num
        previous = [-1] * adj_list.vertexes_num

        distances[start_vertex] = 0

        if enter_callback:
            enter_callback(start_vertex)
        if leave_callback:
            leave_callback(start_vertex)

        while len(planned) > 0:
            u = planned.pop()
            for v in adj_list.get_edges(u, reverse=False):
                if colors[v] == white:
                    distances[v] = distances[u] + 1
                    previous[v] = u
                    colors[v] = gray
                    planned.insert(0, v)

                    if enter_callback:
                        enter_callback(v)

            colors[u] = black

            if leave_callback:
                leave_callback(u)

        return distances, previous

    @staticmethod
    def bfs_order(adj_list: AdjacencyList, start_vertex: int):
        visited = [False] * adj_list.vertexes_num
        queue = [start_vertex]
        visited[start_vertex] = True
        order = []
        while queue:
            v = queue.pop(0)
            order.append(v)
            for w in adj_list.get_edges(v, reverse=False):
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
        return order


def main():
    adj_list = AdjListBuilder.build(is_directed=False)
    start_vertex = int(sys.stdin.readline().strip())

    order = GraphCrawler.bfs_order(adj_list, start_vertex)
    print(' '.join(map(str, order)))


if __name__ == '__main__':
    main()





