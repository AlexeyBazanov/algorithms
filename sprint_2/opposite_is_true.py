class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def reverse_list(node):
    if node.prev:
        node.prev = None

    head = node

    while node:
        node.prev, node.next = node.next, node.prev
        head = node
        node = node.prev

    return head


if __name__ == '__main__':
    first_node = DoubleConnectedNode('first', None)

    second_node = DoubleConnectedNode('second', first_node)

    first_node.prev = second_node

    third_node = DoubleConnectedNode('third', second_node)

    second_node.prev = third_node

    head_node = DoubleConnectedNode('head', third_node)

    third_node.prev = head_node

    head_node = reverse_list(second_node)

    # first second third head

    # print(second_node.prev.value)

    while head_node:
        print(head_node.value, end=' -> ' if head_node.next else '')
        head_node = head_node.next

    # while first_node:
    #     print(first_node.value, end=' -> ' if first_node.prev else '')
    #     first_node = first_node.prev

# third second first head
