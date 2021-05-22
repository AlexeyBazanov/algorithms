import sys


def find_day(days, price, left, right):

    mid = (left + right) // 2

    # print("L:{0}, R:{1}, M:{2}".format(left, right, mid))

    if (right - left) == 1:
        if days[left] >= price:
            return left + 1
        else:
            right_index = right-1 if right == len(days) else right

            if days[right_index] >= price:
                return right + 1

            return -1

    if days[mid] < price:
        # print("M:{0} < P:{1}".format(days[mid], price))
        return find_day(days, price, mid, right)

    else:
        # print("M:{0} >= P:{1}".format(days[mid], price))
        return find_day(days, price, left, mid)


def main():
    days_amount = int(sys.stdin.readline().strip())
    days = sys.stdin.readline().strip().split(' ')
    days = [int(i) for i in days]
    price = int(sys.stdin.readline().strip())

    print('{0} {1}'.format(find_day(days, price, 0, days_amount), find_day(days, price * 2, 0, days_amount)))


main()
