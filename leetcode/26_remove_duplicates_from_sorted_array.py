from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_num = nums[0] - 1
        nums_count = len(nums)

        for index in range(nums_count):
            reverse_index = index - nums_count
            if nums[reverse_index] <= prev_num:
                del nums[reverse_index]
            prev_num = nums[reverse_index]

        return len(nums)
