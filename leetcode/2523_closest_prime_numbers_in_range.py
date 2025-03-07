from itertools import combinations
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

        prime_pair = combinations(prime_list, 2)

        target = []
        min_diff = right - left + 1
        for pair in prime_pair:
            if pair[1] - pair[0] < min_diff:
                min_diff = pair[1] - pair[0]
                target = [pair[0], pair[1]]
        return target

