def solution(node, value):
    index = 0

    while node:
        if node.value == value:
            return index
        node = node.next_item
        index += 1

    return -1
