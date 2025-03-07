from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target_time = len(nums) // 2
        count_dict = {}

        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1

            if count_dict[num] > target_time:
                return num

        return 0