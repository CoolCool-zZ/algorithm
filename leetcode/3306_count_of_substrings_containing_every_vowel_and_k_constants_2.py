class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        consonant_count = 0
        vowel_count = 0

        result = 0
        extra_left, left = 0, 0
        frequencies = {}
        for right, right_char in enumerate(word):
            # 오른쪽으로 이동하면서 추가
            if right_char in "aeiou":
                frequencies[right_char] = frequencies.get(right_char, 0) + 1
                if frequencies[right_char] == 1:
                    vowel_count += 1
            else:
                consonant_count += 1

            # 만약 자음이 개수 초과하면 왼쪽에서부터 줄이기
            while consonant_count > k:
                left_char = word[left]
                if left_char in "aeiou":
                    frequencies[left_char] -= 1
                    if frequencies[left_char] == 0:
                        vowel_count -= 1
                else:
                    consonant_count -= 1
                # 실제로 left 자체를 움직일 때 extra_left 초기화
                left += 1
                extra_left = 0

            # 그렇게 자음 개수만 줄인 후, 왼쪽에 있는 게 모음이라서 추가적으로 더 줄일 수 있는지 확인
            while (
                vowel_count == 5
                and consonant_count == k
                and left < right
                and word[left] in "aeiou"
                and frequencies[word[left]] > 1
            ):
                extra_left += 1
                frequencies[word[left]] -= 1
                left += 1

            # 왼쪽 모음을 추가적으로 줄였을 때의 구성을 포함해서 카운트
            if consonant_count == k and vowel_count == 5:
                result += 1 + extra_left

        return result


def main():
    # define test case
    word = "aadieuoh"
    k = 1

    # run
    solution = Solution()
    result = solution.countOfSubstrings(word, k)
    print(result)


if __name__ == "__main__":
    main()
