def find_x(array, x):
    for i in array:
        if i == x:
            return i
    return -1


numbers = [1, 3, 4, 5, 2, 1, 6, 7]
needle = 3

print(find_x(numbers, needle))

# 1 2 1 3 2
# 1 2, 1 1, 1 3, 1 2
# 1 2, 1 1, 1 3, 1 2
# 1 2, 1 1, 1 3, 1 2
# 1 2, 1 1, 1 3, 1 2
# 1 2, 1 1, 1 3, 1 2
