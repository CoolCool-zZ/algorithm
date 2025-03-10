from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        nums = [True] * (right + 1)
        nums[0] = False
        nums[1] = False

        for num in range(2, right + 1):
            if nums[num] == True:
                for j in range(2, right // num + 1):
                    nums[num * j] = False

        prime_list = []
        for index in range(left, right + 1):
            if nums[index]:
                prime_list.append(index)

        if len(prime_list) == 2:
            return prime_list
        elif len(prime_list) < 2:
            return [-1, -1]

        target = []
        min_diff = right - left + 1
        for index in range(len(prime_list)):
            if index == len(prime_list) - 1:
                break

            if prime_list[index + 1] - prime_list[index] < min_diff:
                min_diff = prime_list[index + 1] - prime_list[index]
                target = [prime_list[index], prime_list[index + 1]]
        return target


def main():
    # define test case
    left = 69346
    right = 69379

    # run
    solution = Solution()
    result = solution.closestPrimes(left, right)
    print(result)


if __name__ == "__main__":
    main()
