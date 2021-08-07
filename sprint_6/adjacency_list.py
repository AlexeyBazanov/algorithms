import sys


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
    edges.sort()
    return edges


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

    for i in range(1, vertex_num+1):
        vertex_pow = get_vertex_pow(adj_list, i)
        edges = get_vertex_edges(adj_list, i)

        if vertex_pow > 0:
            print('{0} {1}'.format(str(vertex_pow), ' '.join(map(str, edges))))
        else:
            print('0')


if __name__ == '__main__':
    main()
