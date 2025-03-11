from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        able_to_reach = []
        for index, jump in enumerate(nums):
            able_to_reach.append(index + jump)

        maximum_to_reach = 0
        for index, able in enumerate(able_to_reach):
            if index <= maximum_to_reach:
                maximum_to_reach = max(maximum_to_reach, able)
            if maximum_to_reach >= len(nums) - 1:
                return True

        return False
