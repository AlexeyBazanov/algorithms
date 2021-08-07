class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(node: Node) -> int:
    return find_max(node, -1)


def find_max(node: Node, current_max) -> int:
    if node.value > current_max:
        current_max = node.value

    left_max = 0
    right_max = 0

    if node.left is not None:
        left_max = find_max(node.left, current_max)

    if node.right is not None:
        right_max = find_max(node.right, current_max)

    return max(current_max, left_max, right_max)

