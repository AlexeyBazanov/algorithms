import sys
import cProfile as profile


def get_fours(numbers, needle):
    result = set()
    sums = {}
    n = len(numbers)

    for a in range(n):
        for b in range(a+1, n):
            summa = numbers[a] + numbers[b]

            if summa > needle:
                continue

            if summa in sums:
                sums[summa].append([a, b])
            else:
                sums[summa] = [[a, b]]

    for c in range(n):
        for d in range(c+1, n):
            diff = needle - numbers[c] + numbers[d]

            if diff > needle:
                continue

            if diff in sums:
                for ab_idx in sums[diff]:
                    if ab_idx[0] != c and ab_idx[1] != d and ab_idx[0] != d and ab_idx[1] != c:
                        four = [ab_idx[0], ab_idx[1], numbers[c], numbers[d]]
                        four.sort()
                        result.add(' '.join(map(str, four)))

                        # result.append(four)

    return result


# if __name__ == '__main__':
    # pr = profile.Profile()
    # sys.stdin.readline()

    # needle = int(sys.stdin.readline().strip())
    # numbers = [int(i) for i in sys.stdin.readline().strip().split(' ')]

    # pr.enable()
    # fours = get_fours(numbers, needle)
    # pr.disable()

    # pr.dump_stats('profile.pstat')

    # print(fours)

    # for f in fours:
        # print(f[0])
        # print(fours[f])


