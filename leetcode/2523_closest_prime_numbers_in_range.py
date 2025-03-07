from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # TODO - Result = Time Limit Exceeded
        right_square_root = int(right ** 0.5)

        nums = list(range(left, right + 1))
        for divisor in range(2, right_square_root + 1):
            for dividend in nums:
                if dividend > divisor and dividend % divisor == 0:
                    nums.remove(dividend)

        if len(nums) == 2:
            return nums
        elif len(nums) < 2:
            return [-1, -1]

        target = []
        min_diff = right - left + 1
        for index in range(len(nums)):
            if index == len(nums) - 1:
                break

            if nums[index + 1] - nums[index] < min_diff:
                min_diff = nums[index + 1] - nums[index]
                target = [nums[index], nums[index + 1]]
        return target
