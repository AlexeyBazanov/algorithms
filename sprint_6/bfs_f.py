import sys


def create_adj_list(size):
    return [None] * (size + 1)


def add_to_adj_list(adj_list, v_from, v_to):
    if adj_list[v_from] is None:
        adj_list[v_from] = []
    adj_list[v_from].append(v_to)


def get_vertex_edges(adj_list, v, reverse=False):
    if adj_list[v] is None:
        return []
    edges = adj_list[v]
    edges.sort(reverse=reverse)
    return edges


def bfs(adj_list, start_vertex):
    order = []
    vertexes_num = len(adj_list)
    white = 0
    gray = 1
    black = 2
    colors = [white] * vertexes_num
    colors[start_vertex] = gray

    planned = [start_vertex]

    while len(planned) > 0:
        u = planned.pop(0)
        order.append(u)
        for v in get_vertex_edges(adj_list, u):
            if colors[v] == white:
                colors[v] = gray
                planned.append(v)

        colors[u] = black

    return order


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

    order = bfs(adj_list, start_vertex)

    print(' '.join(map(str, order)))


if __name__ == '__main__':
    main()