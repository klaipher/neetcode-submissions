class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for current_price in prices:
            if current_price < min_price:
                min_price = current_price
            else:
                max_profit = max(max_profit, current_price - min_price)
        return max_profit
