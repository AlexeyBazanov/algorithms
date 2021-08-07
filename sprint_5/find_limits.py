class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root: Node) -> bool:
    limits = bst_limits(root)
    return is_bst(root, limits[0], limits[1])


def isBST(root, l=None, r=None):
    if root is None:
        return True

    if l is not None and root.value <= l.value:
        return False

    if r is not None and root.value >= r.value:
        return False

    return isBST(root.left, l, root) and isBST(root.right, root, r)


def is_bst(node: Node, minimum: int, maximum: int) -> bool:
    if node is None:
        return True

    if node.value < minimum or node.value > maximum:
        return False

    return is_bst(node.left, minimum, node.value) and is_bst(node.right, node.value, maximum)


def bst_limits(node: Node, minimum: int = None, maximum: int = None):
    if maximum is None or node.value > maximum:
        maximum = node.value
    if minimum is None or node.value < minimum:
        minimum = node.value

    left_limits = [minimum, maximum]
    right_limits = [minimum, maximum]

    if node.left is not None:
        left_limits = bst_limits(node.left, minimum, maximum)

    if node.right is not None:
        right_limits = bst_limits(node.right, minimum, maximum)

    minimum = min(minimum, left_limits[0], right_limits[0])
    maximum = max(maximum, left_limits[1], right_limits[1])

    return [minimum, maximum]


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    print(solution(node5))
    print(isBST(node5))


test()
