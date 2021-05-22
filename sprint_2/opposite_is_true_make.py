def solution(node):
    if node.prev:
        node.prev = None

    head = node

    while node:
        node.prev, node.next = node.next, node.prev
        head = node
        node = node.prev

    return head
