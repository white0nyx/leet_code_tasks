class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float("inf")
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


day_prices = [2, 2, 7, 4, 5, 6, 5]

print(Solution().maxProfit(day_prices))
