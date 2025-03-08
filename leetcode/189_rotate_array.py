from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotate_right_count = k % len(nums)
        original_nums = nums.copy()

        for index in range(len(nums)):
            new_index = (index + rotate_right_count) % len(nums)
            nums[new_index] = original_nums[index]
