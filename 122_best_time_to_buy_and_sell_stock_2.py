from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0
        local_min = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                result += prices[i-1] - local_min
                local_min = prices[i]

        result += prices[-1] - local_min
        return result


week_prices = [1,2,3,4,5]

print(Solution().maxProfit(week_prices))
