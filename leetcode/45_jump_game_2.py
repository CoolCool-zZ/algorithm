from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        able_to_reach = nums.copy()

        for index, jump in enumerate(able_to_reach):
            able_to_reach[index] += index

        for index, able in enumerate(able_to_reach):
            if able >= len(nums) - 1:
                return self.jump(nums[: index + 1]) + 1

        return 0
