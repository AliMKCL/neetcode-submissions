class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution: Sliding window.
        # Start date should be the lowest cost around
        # End date should be the highest cost around.

        if len(prices) == 1:
            return 0

        start = 0
        end = 1
        max_profit = 0


        while end < len(prices):
            if prices[end] < prices[start]:
                start = end
            
            if prices[end] - prices[start] > max_profit:
                max_profit = prices[end] - prices[start]

            end += 1
        
        return 0 if max_profit < 0 else max_profit

            


