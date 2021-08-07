def print_range(node: Node, l: int, r: int):
    result = []
    get_range(node, l, r, result)
    result.sort()
    for i in result:
        print(i)


def get_range(root: Node, left: int, right: int, result: list):
    if left <= root.value <= right:
        result.append(root.value)
    if root.left and root.value >= left:
        get_range(root.left, left, right, result)
    if root.right and root.value <= right:
        get_range(root.right, left, right, result)
