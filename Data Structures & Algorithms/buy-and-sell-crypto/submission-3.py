class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        index = 0
        profit = 0

        while index < len(prices):
            
            for i in prices[index:]:
                if i > prices[index]:
                    profit = i - prices[index]
                    res = max(profit, res)
            index += 1
            
        return res


