def find_lowest_pair(numbers):
    lowes_pair = [numbers[0], numbers[1]]
    array_len = len(numbers)
    iterate_pos = 1
    iterations = 0

    for i in numbers:
        for n in range(iterate_pos, array_len):
            # print(str(i) + " " + str(numbers[n]))
            if (i + numbers[n]) < (lowes_pair[0] + lowes_pair[1]):
                lowes_pair[0] = i
                lowes_pair[1] = numbers[n]
            iterations += 1
        iterate_pos += 1
    print(iterations)
    return lowes_pair


# 1 3 2 4 1
print(find_lowest_pair([1, 2, 3, 4, 1, 6, 8, 4, 3, 5]))
