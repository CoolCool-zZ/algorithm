from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff_prices = []
        for index in range(len(prices)):
            if index == 0:
                continue
            diff_prices.append(prices[index] - prices[index - 1])

        profit = 0
        for diff in diff_prices:
            profit = max(profit, profit + diff)

        return profit
