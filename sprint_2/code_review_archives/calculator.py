import sys

"""
ID посылки - 49200057

-- ПРИНЦИП РАБОТЫ --
Почти весь алгоритм рассказали в описании к задаче :(
Если подытожить, то нам нужно пробежаться по строке слева направо.
Если нам встречается цифра, то конкатенируем ее в переменную. 
Если нам встречается пробел, то мы проверяем, не пуста ли переменная 
с конкатенированными цифрами. 
Если не пуста - кладем число записанное в эту переменную на вершину стека. 
Если нам встречается знак операции, то мы должны сначала проверить не является ли он знаком числа.
Если это знак "-" и следом за ним в строке находится цифра, то записываем его в переменную для числа.
В ином случае мы берем два числа с вершины стека и производим над ними вычисление. 
Результат вычисления кладем на вершину того же стека, в котором храним числа из строки нотации.
Так идем пока строка не кончится. Потом возвращаем верхний элемент стека (по условию задачи).
Нам могут встретится следующие исключительные ситуации: деление на ноль и 
некорректная запись в нотации: когда передано недостаточное кол-во чисел для вычисления
(в таком случе мы попытаемся забрать число с вершины пустого стека). 
В обеих ситаациях я решил вернуть None.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Алгоритму необходимо один раз перебрать все символы в строке, т.е. выполнить O(n) операций. 
На каждой итерации мы можем либо положить элемент в стек, либо достать два элемента из стека.
Каждая операция выполняется за O(1) и не влияет на общую сложность.
В случае, если строка записана верно, алгоритм завершится за O(n).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Так как мы не используем массив для промежуточного хранения элементов нотации,
алгоритм будет потреблять O(n) памяти, где n - вес строки с нотацией.
"""


class Calculator:
    def __init__(self):
        self.__clear()

    def __clear(self):
        """Метод сброса переменных для калькуляции выражения"""
        self.__current_index = 0
        self.__numbers = []
        self.__last_number = ''

    def calculate(self, notation):
        try:
            self.__iterate_notation(notation)
        except ZeroDivisionError:
            return None
        except IndexError:
            return None
        else:
            return self.__return_result()
        finally:
            self.__clear()

    def __iterate_notation(self, notation):

        notation_len = len(notation)

        for i in range(notation_len):

            self.__current_index = i
            notation_item = notation[i]

            if self.__is_number(notation_item):
                self.__concatenate_last_number(notation_item)
            elif self.__is_space(notation_item) and self.__last_number_exist():
                self.__save_last_number()
            elif self.__is_operation(notation_item):
                if self.__is_number_sign(notation_item, notation):
                    self.__concatenate_last_number(notation_item)
                else:
                    self.__calculate_last_two_numbers(notation_item)

    def __save_last_number(self):
        """Метод сохраняющий промежуточное число в стек"""
        self.__numbers.append(int(self.__last_number))
        self.__last_number = ''

    def __concatenate_last_number(self, item):
        """Метод конкатенирующий цифры и знак к промежуточноему числу"""
        self.__last_number += item

    def __return_result(self):
        """Метод возвращающий результат.
        В случае если у нас осталось неиспользованное промежуточное число - вернет его,
        иначе вернет последнее число из стека чисел (если стек не пуст, иначе вернет None).
        """
        if self.__last_number_exist():
            return int(self.__last_number)
        else:
            return self.__numbers.pop() if len(self.__numbers) else None

    def __calculate_last_two_numbers(self, operator):
        second_operand = self.__numbers.pop()
        first_operand = self.__numbers.pop()
        result = self.__calculate(first_operand, second_operand, operator)
        self.__numbers.append(result)

    def __calculate(self, first_operand, second_operand, operation):
        if self.__is_addition(operation):
            return first_operand + second_operand
        elif self.__is_subtraction(operation):
            return first_operand - second_operand
        elif self.__is_multiplication(operation):
            return first_operand * second_operand
        elif self.__is_division(operation):
            return first_operand // second_operand

    def __last_number_exist(self):
        return self.__last_number

    def __is_number_sign(self, notation_item, notation):
        return self.__is_subtraction(notation_item) and self.__next_item_is_number(notation)

    def __next_item_is_number(self, notation):
        return self.__current_index + 1 <= len(notation) - 1 \
               and self.__is_number(notation[self.__current_index + 1])

    def __is_operation(self, notation_item):
        return self.__is_addition(notation_item) \
               or self.__is_subtraction(notation_item) \
               or self.__is_division(notation_item) \
               or self.__is_multiplication(notation_item)

    def __is_number(self, notation_item):
        return notation_item in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __is_space(self, notation_item):
        return notation_item == ' '

    def __is_addition(self, operation):
        return operation == '+'

    def __is_subtraction(self, operation):
        return operation == '-'

    def __is_multiplication(self, operation):
        return operation == '*'

    def __is_division(self, operation):
        return operation == '/'


def main():
    calculator = Calculator()
    notation = sys.stdin.readline().strip()
    print(calculator.calculate(notation))


if __name__ == '__main__':
    main()
