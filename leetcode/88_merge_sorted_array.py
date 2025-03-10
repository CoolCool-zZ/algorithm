from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        only_nums1 = nums1[:m]
        index1 = 0
        index2 = 0

        if n == 0:
            return
        elif m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        for i in range(m + n):
            if index1 >= m:
                nums1[i] = nums2[index2]
                index2 += 1
            elif index2 >= n:
                nums1[i] = only_nums1[index1]
                index1 += 1
            elif only_nums1[index1] > nums2[index2]:
                nums1[i] = nums2[index2]
                index2 += 1
            else:
                nums1[i] = only_nums1[index1]
                index1 += 1

        print(f"nums1: {nums1}")


def main():
    # define test case
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1

    # run
    solution = Solution()
    solution.merge(nums1, m, nums2, n)


if __name__ == "__main__":
    main()
