from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # TODO - Result = Time Limit Exceeded
        right_square_root = int(right ** 0.5)

        nums = [True] * (right + 1)
        for dividend in range(left, right + 1):
            if nums[dividend] == False:
                continue

            for divisor in range(2, right_square_root + 1):
                if dividend > divisor and dividend % divisor == 0:
                    nums[dividend] = False

        prime_list = []
        for index in range(left, right + 1):
            if nums[index]:
                prime_list.append(index)

        if len(prime_list) == 2:
            return nums
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
