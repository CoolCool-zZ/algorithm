class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        original_nums_count = len(nums)
        delete_index = []
        for index in range(original_nums_count):
            if nums[index] == val:
                delete_index.append(index)

        delete_index.reverse()
        for index in delete_index:
            del nums[index]

        return len(nums)
