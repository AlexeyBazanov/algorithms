import sys

"""
ID посылки - 49129246

-- ПРИНЦИП РАБОТЫ --
Чтобы понять суть задачи, можно представить себе очередь в поликлинику. 
Те люди, кто пришел без записи, спрашивают, кто последний и встают за ним.
Те, кто пришел по записи встают в начало очереди.   
Представим, что мы наблюдаем за этой очередью со стороны. 
Начало очереди находится слева от нас, а конец - справа. 
Представим данную очередь как массив с индексами от нуля до N - 1, где N это размер очереди. 
Обозначим позицию первого человека в очереди как H (head), а последнего как T (tail).
Чтобы вызвать в кабинет первого пациента - нужно обратится к позиции H: 
после этого первым в очереди станет человек на позиции H + 1.
Чтобы вызвать последнего пациента нужно обратится к позиции T: 
после этого последним пациентом станет человек на позиции T - 1.
Человек который придет по записи встанет на позицию H - 1, а человек который придет без записи - на T + 1. 
Если бы очередь была бесконечна, на этом можно было бы закончить описание алгоритма.
Но так как наша очередь ограничена, мы ее "закольцуем". 
Т.е. если мы ставим нового пациента в начало очереди, и его позиция (H - 1) становится меньше нуля,
то мы помещаем его на позицию N - 1.
Если же мы ставим нового пациента в конец очереди, и его позиция (T + 1) становится больше N - 1, 
то мы помещаем его на позицию с нулевым индексом.
Если приходит новый пациент и хочет встать в очередь, а все места в ней уже кончились, 
мы сообщим ему об этом, выдав исключение :) 
Если же врач будет кричать "следующий!", а перед дверью не останется пациентов, 
мы тоже сообщим ему об этом при помощи исключения.    

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Вставка в Дек занимает O(1), извлечение тоже O(1), следовательно скорость выполнения - O(1) ??

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Мы используем для хранения массив фиксированного размера, а
массив, содержащий k элементов, занимает O(k) памяти.
Следоваетльно дек будет занимать O(n) памяти. 
"""


class Deque:
    def __init__(self, size):
        """
        Конструктор объекта Deque
        :param size: integer, должен быть не отрицательным
        """
        self.__items = [None] * size  # Очередь
        self.__max_size = size  # Максимальный размер очереди
        self.__size = 0  # Текущий размер очереди
        self.__head = 0  # Индекс начала очереди
        self.__tail = 0  # Индекс конца очереди

    def push_back(self, item):
        """Метод добавления элемента в конец очереди"""
        self.__check_overflow()
        self.__push(item, self.__tail)
        self.__increase_tail()

    def pop_back(self):
        """Метод получения элемента из конца очереди"""
        self.__check_emptying()
        self.__reduce_tail()
        return self.__pop(self.__tail)

    def push_front(self, item):
        """Метод добавления элемента в начало очереди"""
        self.__check_overflow()
        self.__reduce_head()
        self.__push(item, self.__head)

    def pop_front(self):
        """Метод получения элемента из начала очереди"""
        self.__check_emptying()
        item = self.__pop(self.__head)
        self.__increase_head()
        return item

    def is_full(self):
        """Заполнена ли очередь"""
        return self.__size == self.__max_size

    def is_empty(self):
        """Пуста ли очередь"""
        return self.__size == 0

    def size(self):
        return self.__size

    def items(self):
        return self.__items

    def head(self):
        return self.__head

    def tail(self):
        return self.__tail

    def max_size(self):
        return self.__max_size

    def __push(self, item, index):
        """Общий метод вставки элемента"""
        self.__items[index] = item
        self.__size += 1

    def __pop(self, index) -> object:
        """Общий метод получения элемента"""
        item = self.__items[index]
        self.__items[index] = None
        self.__size -= 1

        return item

    def __check_overflow(self):
        """Метод проверки переполнения. Выбрасывает исключение IndexError в случае переполнения очереди."""
        if self.is_full():
            raise IndexError

    def __check_emptying(self):
        """Метод проверки пустоты. Выбрасывает исключение IndexError в случае попытки достать из пустой очереди."""
        if self.is_empty():
            raise IndexError

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


class CommandHandler:
    def __init__(self, deque_size):
        self.deque = Deque(deque_size)

    """
    Метод передающий обработку комманды другим методам класса.
    Обрабатывает исключения для добавления в полный дек
    и взятие из пустого дека.
    """
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

