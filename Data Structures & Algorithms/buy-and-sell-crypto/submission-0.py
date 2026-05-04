class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        index = 0
        profit = 0

        while index < len(prices):

            for i in prices[index:]:
                if i > prices[index]:
                    profit = i - prices[index]
                    max_profit = max(profit, max_profit)
            index += 1
        
        return max_profit
        
