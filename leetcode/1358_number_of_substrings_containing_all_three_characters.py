class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc_count = {"a": 0, "b": 0, "c": 0}

        result = 0
        left = 0
        for right in range(len(s)):
            abc_count[s[right]] += 1

            while abc_count["a"] > 0 and abc_count["b"] > 0 and abc_count["c"] > 0:
                result += len(s) - right
                abc_count[s[left]] -= 1
                left += 1

        return result


def main():
    # define test case
    s = "abcabc"

    # run
    solution = Solution()
    result = solution.numberOfSubstrings(s)
    print(result)


if __name__ == "__main__":
    main()
