import sys


def get_longest_unique_substr(string, charset_len=256):
    n = len(string)

    if n == 0:
        return 0

    cur_len = 1
    max_len = 1
    visited = [-1] * charset_len

    visited[ord(string[0])] = 0

    for i in range(1, n):
        cur_char = ord(string[i])
        prev_index = visited[cur_char]

        if prev_index == -1 or (i - cur_len > prev_index):
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len

            cur_len = i - prev_index

        visited[cur_char] = i

    if cur_len > max_len:
        max_len = cur_len

    return max_len


def main():
    string = sys.stdin.readline().strip()
    print(get_longest_unique_substr(string))


if __name__ == '__main__':
    main()





