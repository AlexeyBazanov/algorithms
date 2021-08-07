import sys
import random


def is_comb_possible(four, nums_counter_map):
    comp_counter_map = {}

    for i in four:
        if i not in comp_counter_map:
            comp_counter_map[i] = 0
        comp_counter_map[i] += 1

    for i in comp_counter_map:
        if comp_counter_map[i] > nums_counter_map[i]:
            return False

    return True


def get_fours(numbers, needle):
    sums = {}
    nums_counter = {}
    fours = set()
    n = len(numbers)

    for a in range(n):
        for b in range(a + 1, n):
            s = numbers[a] + numbers[b]
            if s not in sums:
                sums[s] = set()
            sums[s].add(tuple(sorted([numbers[a], numbers[b]])))

        if numbers[a] not in nums_counter:
            nums_counter[numbers[a]] = 0
        nums_counter[numbers[a]] += 1

    print(sys.getsizeof(sums))
    print(len(sums))

    exit()

    for s1 in sums:
        for s2 in sums:
            if s1 + s2 == needle:
                for s1_nums in sums[s1]:
                    for s2_nums in sums[s2]:
                        four = [s1_nums[0], s1_nums[1], s2_nums[0], s2_nums[1]]
                        if is_comb_possible(four, nums_counter):
                            fours.add(tuple(sorted(four)))

    fours = sorted(fours, key=lambda i: (i[0], i[1], i[2], i[3]))

    # print(sys.getsizeof(fours) / 1024 / 1024)

    return fours


def main():
    nums_cnt = int(sys.stdin.readline())

    if nums_cnt == 0:
        print(0)
        exit()

    needle = int(sys.stdin.readline().strip())
    numbers = [int(i) for i in sys.stdin.readline().strip().split(' ')]

    fours = get_fours(numbers, needle)

    # print(len(fours))
    #
    # for four in fours:
    #     print(' '.join(map(str, four)))


if __name__ == '__main__':
    main()
    # nums = ''
    #
    # for i in range(1000):
    #     integer = random.randint(-10**9, 10**9)
    #     nums += str(integer) + " "
    #
    # print(nums)
