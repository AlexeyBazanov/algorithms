import sys


def is_odd_equal(str1, str2):
    map1 = {}
    map2 = {}

    str1_len = len(str1)
    str2_len = len(str2)

    if str1_len != str2_len:
        return False

    for i in range(str1_len):
        let1 = str1[i]
        let2 = str2[i]

        if let1 in map1 and map1[let1] != let2:
            return False

        if let2 in map2 and map2[let2] != let1:
            return False

        map1[let1] = let2
        map2[let2] = let1

    return True


def main():
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    print('YES' if is_odd_equal(str1, str2) else 'NO')


if __name__ == '__main__':
    main()
