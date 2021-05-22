class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.max_size = size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def push(self, item):
        if not self.is_full():
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item

    def peek(self):
        return self.queue[self.head]
