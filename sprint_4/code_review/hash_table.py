import sys


"""
-- ID ПОСЫЛКИ - 52019143 --

-- ПРИНЦИП РАБОТЫ --
Создаем класс, содержащий поле - массив, в котором будут хранится данные нашей таблицы.
Так же класс будем хранить занятые ячейки массива с данными, кол-во хранимых значений, 
текущую длину массива. 

В классе создаем методы интерфесы для внесения, получения и удаления данных. 
Так же создаем служебные методы для перезаписи существующих данных,
подсчета хэша ячейки, определения переполнения массива с данными, реалокации массива.

При вставке мы будем проверять не переполнен ли массив с данными по формуле
(кол-во занятых ячеек массива > длина массива / 2).
Если массив данных переполнен мы его удваиваем и переносим туда данные.
Затем мы считаем индекс текущей ячейки взяв остаток от деления переданного в метод ключа на длину массива.
Проверяем есть ли значение в данной ячейки. Если нет - создаем там массив, в котором храним другой массив с двумя значения: 
[переданный ключ, переданное значение].
Если занят то мы сначала итерируем массив с ключами-значениями, проверяем нет ли там переданного в метод ключа, 
если есть - перезаписываем значение.
Если мы ничего не перезаписале на прошлом этапе - добавляем еще один массив [ключ, значение]. 

При удалении сначала проверяем есть ли запись по хэшу переданного ключа. 
Если ячейка не пуста: создаем новый массив, итерируем массив в ячейке, кладем в новый массив все значения,
ключ которых не равен переданному в метод ключу. Если получившийся массив не пуст - обновляем текущий массив. 
Если пуст - обнуляем значение. 
Возвращаем либо сохраненное заранее значение удаленного элемента, либо None.

При получении элемента, сначала проверяем пуста ли ячейка.
Если да - возвращаем None. Если нет - итерируем ее е возвращаем значение элемента, 
индекс которого равен переданному в метод индексу.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Вставка происходит за O(1) в лучшем случае, 
но в особых случаяк, когда таблица переполнена и нужно создать новую - O(n).

Удаление и чтение происходит за O(1) в среднем и за O(n) в худшем (если по какой то причине в одну ячейку записано много значений).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Понадобится O(n) памяти.
"""


class HashTable:
    def __init__(self, init_length=256):
        self.buckets = [None] * init_length
        self.buckets_fill = 0
        self.length = init_length
        self.size = 0

    def put(self, key, value):
        if self.is_full():
            self.double()

        bucket_key = self.get_bucket_key(key)

        if self.buckets[bucket_key] is None:
            self.buckets[bucket_key] = [[key, value]]
            self.buckets_fill += 1
            self.size += 1
        else:
            overwritten = self.overwrite(bucket_key, key, value)
            if not overwritten:
                self.buckets[bucket_key].append([key, value])
                self.size += 1

    def overwrite(self, bucket_key, item_key, item_val):
        if self.buckets[bucket_key] is None:
            return False

        replaced = False
        bucket_len = len(self.buckets[bucket_key])

        for i in range(bucket_len):
            current_key = self.buckets[bucket_key][i][0]
            if item_key == current_key:
                self.buckets[bucket_key][i][1] = item_val
                replaced = True

        return replaced

    def get(self, key):
        bucket = self.buckets[self.get_bucket_key(key)]

        if bucket is None:
            return None

        for k, v in bucket:
            if k == key:
                return v

        return None

    def delete(self, key):
        bucket_key = self.get_bucket_key(key)

        if self.buckets[bucket_key] is None:
            return None

        new_list = []
        deleted_value = None

        for k, v in self.buckets[bucket_key]:
            if k == key:
                deleted_value = v
                continue
            new_list.append([k, v])

        if new_list:
            self.buckets[bucket_key] = new_list
        else:
            self.buckets[bucket_key] = None
            self.buckets_fill -= 1

        self.size -= 1
        return deleted_value

    def is_full(self):
        return self.buckets_fill > self.length / 2

    def double(self):
        new_length = self.length * 2
        new_table = HashTable(new_length)

        for bucket in self.buckets:
            if bucket is None:
                continue

            for key, value in bucket:
                new_table.put(key, value)

        self.length = new_length
        self.buckets = new_table.buckets
        self.buckets_fill = new_table.buckets_fill

    def get_bucket_key(self, key):
        return hash(key) % self.length


def handle_command(command, hash_table):
    command_args = command.split(' ')
    command_name = command_args[0]

    if command_name == 'get':
        print(hash_table.get(int(command_args[1])))
    elif command_name == 'put':
        hash_table.put(int(command_args[1]), command_args[2])
    elif command_name == 'delete':
        print(hash_table.delete(int(command_args[1])))


def main():
    hash_table = HashTable(init_length=1024)
    commands_number = int(sys.stdin.readline().strip())

    for i in range(commands_number):
        command = sys.stdin.readline().strip()
        handle_command(command, hash_table)


if __name__ == '__main__':
    main()
