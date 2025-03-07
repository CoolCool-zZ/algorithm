from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_num = nums[0] - 1
        nums_count = len(nums)
        appear_count = 0

        for index in range(nums_count):
            reverse_index = index - nums_count
            if nums[reverse_index] == prev_num and appear_count >= 2:
                del nums[reverse_index]
            elif nums[reverse_index] > prev_num:
                appear_count = 0

            prev_num = nums[reverse_index]
            appear_count += 1

        return len(nums)