import sys


def max_draw_sequence(contest_result):
    score = [0, 0]
    round_num = 1
    diffs = {0: [0]}

    for i in contest_result:
        score[i] += 1

        diff = score[0] - score[1]

        if diff in diffs:
            diffs[diff].append(round_num)
        else:
            diffs[diff] = [round_num]

        round_num += 1

    max_diff = 0

    for d in diffs:
        diffs_len = len(diffs[d])

        if not diffs_len > 1:
            pass

        cur_diff = diffs[d][diffs_len-1] - diffs[d][0]

        if cur_diff > max_diff:
            max_diff = cur_diff

    return max_diff


def main():
    sys.stdin.readline().strip()
    contest_result = sys.stdin.readline().strip().split()
    contest_result = [int(i) for i in contest_result]

    print(max_draw_sequence(contest_result))


if __name__ == '__main__':
    main()


