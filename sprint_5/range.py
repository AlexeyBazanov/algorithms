import sys


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def print_range(node: Node, l: int, r: int):
    result = []
    get_range(node, l, r, result)
    result.sort()
    # print(' '.join(map(str, result)))
    for i in result:
        print(i)


def get_range(root: Node, left: int, right: int, result: list):
    if left <= root.value <= right:
        result.append(root.value)
    if root.left and root.value >= left:
        get_range(root.left, left, right, result)
    if root.right and root.value <= right:
        get_range(root.right, left, right, result)


def test():
    # node1 = Node(1, None, None)
    # node2 = Node(4, None, None)
    # node3 = Node(3, node1, node2)
    # node4 = Node(8, None, None)
    # node5 = Node(5, node3, node4)
    #
    # print_range(node5, 3, 5)

    node2 = Node(2, None, None)
    node1 = Node(1, None, node2)

    node82 = Node(8, None, None)
    node81 = Node(8, None, node82)
    node9 = Node(9, node81, None)
    node10 = Node(9, node9, None)

    node5 = Node(5, node1, node10)

    print_range(node5, 2, 8)


test()
