# Найти в массиве два элемента, сумма которых равна X Дано:
# Массив N элементов: [1, 3, 5, 6, 7, 9]
# X - требуемая сумма двух элементов;
# Найти два элемента или сообщить, что таких элементов нет.


# Дана строка, например "aafbaaaaffc" 
# Вывести для каждого символа в ней максимальное количество непрерывных повторений этого символа в строке. Для данной строки, например, результат будет:


# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

# Найти наибольший общий делитель (НОД). Дано:
# Два числа: 81 и 27
# Найти наибольший общий делитель.


# def find_sum(numbers, needle):
#     length = len(numbers)
#     result = []
#
#     for i in range(length):
#         for j in range(i, length):
#             if i + j == needle:
#                 result.append(i)
#                 result.append(j)
#                 return result
#
#
# numbers = [1, 4, 5, 3, 2]
# n = 9
#
# print(find_sum(numbers, n))


# def sum_array(arr, x):
#     diffs = {}
#     for num in arr:
#         diff = x - num
#         diffs[diff] = num
#
#         if diffs.get(diff, None) is not None:
#             return (diff, diffs.get(diff))
