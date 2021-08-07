import sys


class SumFinder:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:  # early termination
                return
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results


def main():
    nums_cnt = int(sys.stdin.readline())

    if nums_cnt == 0:
        print(0)
        exit()

    needle = int(sys.stdin.readline().strip())
    numbers = [int(i) for i in sys.stdin.readline().strip().split(' ')]

    sum_finder = SumFinder()
    fours = sum_finder.fourSum(numbers, needle)

    print(len(fours))

    for four in fours:
        print(' '.join(map(str, four)))


if __name__ == '__main__':
    main()
