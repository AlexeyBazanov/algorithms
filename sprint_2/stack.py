class Stack:
    def __init__(self, size):
        self.items = [None] * size
        self.max_size = size
        self.head = 0
        self.size = 0

    def push(self, item):
        if not self.is_full():
            self.items[self.head] = item
            self.size += 1
            self.head += 1

    def pop(self):
        if self.is_empty():
            return None

        item = self.items[self.head]
        self.items[self.head] = None
        self.size -= 1
        self.head -= 1
        return item

    def peek(self):
        return self.items[self.head]

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0
