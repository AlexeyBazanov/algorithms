import sys


class DequeOld:
    def __init__(self, size):
        self.items = [None] * size  # Очередь
        self.max_size = size  # Максимальный размер очереди
        self.size = 0  # Текущий размер очереди
        self.head = 0  # Индекс начала очереди
        self.tail = 0  # Индекс конца очереди
        self.last_index = size - 1  # Последний индекс очереди
        self.first_index = 0  # Первый индекс очереди
        self.first_index_reverse = -size  # Первый индекс очереди, если считать с конца

    # Добавить элемент в конец очереди
    def push_back(self, item):
        if not self.is_empty():
            self.__tail_reduce()

        self.__push(item, head=False)

    # Достать элемент из конца очереди
    def pop_back(self):
        item = self.__pop(head=False)

        if not self.is_empty():
            self.__tail_increase()

        return item

    # Добавить элемент в начало очереди
    def push_front(self, item):
        if not self.is_empty():
            self.__head_increase()

        self.__push(item, head=True)

    # Достать элемент из начала очереди
    def pop_front(self):
        item = self.__pop(head=True)

        if not self.is_empty():
            self.__head_reduce()

        return item

    # Заполнена ли очередь
    def is_full(self):
        return self.size == self.max_size

    # Пуста ли очередь
    def is_empty(self):
        return self.size == 0

    # Общий метод вставки элемента:
    # вставляет в начало очереди, если head равен True,
    # вставляет в конец очереди, если head равен False.
    # Выкидывает исключение IndexError, если очередь заполнена.
    def __push(self, item, head=True):
        if self.is_full():
            raise IndexError

        push_index = self.head if head else self.tail

        self.items[push_index] = item
        self.size += 1

    # Общий метод получения элемента
    # достает элемент из начала очереди, если head равен True,
    # достает элемент из конца очереди, если head равен False.
    # Выкидывает исключение IndexError, если очередь пуста
    def __pop(self, head=True) -> object:
        if self.is_empty():
            raise IndexError

        pop_index = self.head if head else self.tail

        item = self.items[pop_index]
        self.items[pop_index] = None
        self.size -= 1

        return item

    # Метод увеличивающий индекс, который указывает на начало очереди.
    def __head_increase(self):
        self.head += 1

        if self.head > self.last_index:
            self.head = self.first_index

    # Уменьшить индекс, указывающий на начало очереди
    def __head_reduce(self):
        self.head -= 1

        if self.head == self.first_index_reverse:
            self.head = self.first_index

    # Увеличить индекс, указывающий на конец очереди
    def __tail_increase(self):
        self.tail += 1

        if self.tail > self.last_index:
            self.tail = self.first_index

    # Уменьшить индекс, указывающий на конец очереди
    def __tail_reduce(self):
        self.tail -= 1

        if self.tail == self.first_index_reverse:
            self.tail = self.first_index


class CommandHandler:
    def __init__(self, deque_size):
        self.deque = Deque(deque_size)

    def handle_command(self, command):
        try:
            if command == 'pop_front':
                self.handle_pop_front_command()
            if command == 'pop_back':
                self.handle_pop_back_command()
            if command.find('push_front') != -1:
                self.handle_push_front_command(command)
            if command.find('push_back') != -1:
                self.handle_push_back_command(command)

        except IndexError:
            print('error')
        except ValueError:
            pass

    def handle_pop_front_command(self):
        print(self.deque.pop_front())

    def handle_pop_back_command(self):
        print(self.deque.pop_back())

    def handle_push_front_command(self, command):
        number = int(command.split()[1])
        self.deque.push_front(number)

    def handle_push_back_command(self, command):
        number = int(command.split()[1])
        self.deque.push_back(number)


def main():
    command_count = int(sys.stdin.readline().strip())
    deque_size = int(sys.stdin.readline().strip())
    command_handler = CommandHandler(deque_size)

    while command_count:
        command = sys.stdin.readline().strip()
        command_handler.handle_command(command)
        command_count -= 1


if __name__ == '__main__':
    main()
