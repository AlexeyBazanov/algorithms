import sys


class Deque:
    def __init__(self, size):
        self.__items = [None] * size  # Очередь
        self.__max_size = size  # Максимальный размер очереди
        self.__size = 0  # Текущий размер очереди
        self.__head = 0  # Индекс начала очереди
        self.__tail = 0  # Индекс конца очереди

    def push_back(self, item):
        if self.is_full():
            raise IndexError
        self.__items[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        self.__tail = (self.__tail - 1 + self.__max_size) % self.__max_size
        self.__size -= 1
        return self.__items[self.__tail]

    def push_front(self, item):
        if self.is_full():
            raise IndexError
        self.__head = (self.__head - 1 + self.__max_size) % self.__max_size
        self.__items[self.__head] = item
        self.__size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        item = self.__items[self.__head]
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return item

    def size(self):
        return self.__size

    def items(self):
        return self.__items

    def head(self):
        return self.__head

    def tail(self):
        return self.__tail

    def __increase_head(self):
        self.__head = self.__increase_index(self.__head)

    def __reduce_head(self):
        self.__head = self.__reduce_index(self.__head)

    def __increase_tail(self):
        self.__tail = self.__increase_index(self.__tail)

    def __reduce_tail(self):
        self.__tail = self.__reduce_index(self.__tail)

    def __increase_index(self, index):
        return (index + 1) % self.__max_size

    def __reduce_index(self, index):
        return (index - 1 + self.__max_size) % self.__max_size

    # Заполнена ли очередь
    def is_full(self):
        return self.__size == self.__max_size

    # Пуста ли очередь
    def is_empty(self):
        return self.__size == 0

    # Общий метод вставки элемента:
    # вставляет в начало очереди, если head равен True,
    # вставляет в конец очереди, если head равен False.
    # Выкидывает исключение IndexError, если очередь заполнена.
    def __push(self, item, head=True):
        if self.is_full():
            raise IndexError

        push_index = self.__head if head else self.__tail

        self.__items[push_index] = item
        self.__size += 1

    # Общий метод получения элемента
    # достает элемент из начала очереди, если head равен True,
    # достает элемент из конца очереди, если head равен False.
    # Выкидывает исключение IndexError, если очередь пуста
    def __pop(self, head=True) -> object:
        if self.is_empty():
            raise IndexError

        pop_index = self.__head if head else self.__tail

        item = self.__items[pop_index]
        self.__items[pop_index] = None
        self.__size -= 1

        return item


class CommandHandler:
    def __init__(self, deque_size):
        self.deque = Deque(deque_size)

    # Метод передающий обработку комманды другим методам класса.
    # Обрабатывает исключения для добавления в полный дек
    # и взятие из пустого дека.
    def handle_command(self, command):
        try:
            if command == 'pop_front':
                self.__handle_pop_front_command()
            if command == 'pop_back':
                self.__handle_pop_back_command()
            if command.find('push_front') != -1:
                self.__handle_push_front_command(command)
            if command.find('push_back') != -1:
                self.__handle_push_back_command(command)

        except IndexError:
            print('error')
        except ValueError:
            pass

    def __handle_pop_front_command(self):
        print(self.deque.pop_front())

    def __handle_pop_back_command(self):
        print(self.deque.pop_back())

    def __handle_push_front_command(self, command):
        self.deque.push_front(self.__get_number_from_command(command))

    def __handle_push_back_command(self, command):
        self.deque.push_back(self.__get_number_from_command(command))

    def __get_number_from_command(self, command):
        return int(command.split()[1])


def main():
    command_count = int(sys.stdin.readline().strip())
    deque_size = int(sys.stdin.readline().strip())
    command_handler = CommandHandler(deque_size)

    for i in range(command_count, 0, -1):
        command = sys.stdin.readline().strip()
        command_handler.handle_command(command)


if __name__ == '__main__':
    main()
