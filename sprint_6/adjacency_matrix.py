import sys


def create_adj_matrix(matrix_size):
    matrix = []
    for i in range(matrix_size):
        row = [0] * matrix_size
        matrix.append(row)
    return matrix


def add_edge_to_matrix(matrix, v_from, v_to):
    matrix[v_from][v_to] = 1


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(' '.join(map(str, matrix[i])))


def main():
    info = sys.stdin.readline().strip().split(' ')
    vertex_num = int(info[0])
    edges_num = int(info[1])

    adj_matrix = create_adj_matrix(vertex_num)

    for i in range(edges_num):
        vertex_pair = sys.stdin.readline().strip().split(' ')

        vertex_from = int(vertex_pair[0]) - 1
        vertex_to = int(vertex_pair[1]) - 1

        add_edge_to_matrix(adj_matrix, vertex_from, vertex_to)

    print_matrix(adj_matrix)


if __name__ == '__main__':
    main()
