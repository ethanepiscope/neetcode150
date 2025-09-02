# O(n) time, O(1) space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > profit:
                profit = price - minPrice
        return profit