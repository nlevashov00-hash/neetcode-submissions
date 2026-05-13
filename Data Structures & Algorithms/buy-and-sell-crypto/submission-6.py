class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1

        while l < len(prices) - 1:

            for r in range(l + 1, len(prices)):

                if prices[r] > prices[l]:
                    profit = prices[r] - prices[l]
                    max_profit = max(max_profit, profit)
                
            l += 1
        
        return max_profit
