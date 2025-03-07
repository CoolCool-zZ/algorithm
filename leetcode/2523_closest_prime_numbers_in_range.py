from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # TODO - Result = Time Limit Exceeded
        prime_list = list(range(left, right + 1))
        for divisor in range(2, right + 1):
            for dividend in prime_list:
                if dividend > divisor and dividend % divisor == 0:
                    prime_list.remove(dividend)

        if len(prime_list) == 2:
            return prime_list
        elif len(prime_list) < 2:
            return [-1, -1]

        target = []
        min_diff = right - left + 1
        for index in range(len(prime_list)):
            if index == len(prime_list) - 1:
                break

            if prime_list[index + 1] - prime_list[index] < min_diff:
                min_diff = prime_list[index + 1] - prime_list[index]
                target = [prime_list[index], prime_list[index + 1]]
        return target

