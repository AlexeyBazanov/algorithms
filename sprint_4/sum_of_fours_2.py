import sys


def get_fours(numbers, needle):
    numbers.sort()

    n = len(numbers)
    sums = {}

    print(numbers)

    for a in range(n):
        for b in range(a + 1, n):
            summa = numbers[a] + numbers[b]
            if summa > needle:
                continue
            if summa not in sums:
                sums[summa] = []
            sums[summa].append([a, b])

    # history = set()
    fours = list()

    for s in sums:
        if s + s == needle:
            for i in range(len(sums[s])):
                for j in range(i+1, len(sums[s])):
                    if sums[s][i][0] != sums[s][j][0] and sums[s][i][1] != sums[s][j][1]:
                        four = [sums[s][i][0], sums[s][i][1], sums[s][j][0], sums[s][j][1]]
                        four.sort()
                        fours.append(four)



    print(fours)
    # print(len(sums))

    # for i in range(n):
    #     for j in range(i + 1, n):


def main():
    sys.stdin.readline()

    needle = int(sys.stdin.readline().strip())
    numbers = [int(i) for i in sys.stdin.readline().strip().split(' ')]

    get_fours(numbers, needle)

    # for f in fours:
    #     print(f)


if __name__ == '__main__':
    main()
