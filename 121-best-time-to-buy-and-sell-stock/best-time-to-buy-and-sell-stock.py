class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit_today = price - min_price
            max_profit = max(max_profit, profit_today)
        return max_profit



    
        