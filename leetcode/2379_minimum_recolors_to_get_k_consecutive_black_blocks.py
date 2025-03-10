class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        colored = []
        for index in range(len(blocks)):
            if blocks[index] == "W":
                colored.append(0)
            else:
                colored.append(1)

        if k == len(blocks):
            return k - sum(colored)

        maximum_count = 0
        for index in range(len(blocks) - k + 1):
            temp_count = sum(colored[index : index + k])
            if temp_count == k:
                return 0
            elif temp_count > maximum_count:
                maximum_count = temp_count

        return k - maximum_count


def main():
    # define test case
    blocks = "WWBBBWBBBBBWWBWWWB"
    k = 16

    # run
    solution = Solution()
    result = solution.minimumRecolors(blocks, k)
    print(result)


if __name__ == "__main__":
    main()
