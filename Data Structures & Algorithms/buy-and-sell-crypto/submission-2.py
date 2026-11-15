class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        left = 0

        for right in range(n):
            while prices[left] > prices[right]:
                left += 1
            profit = prices[right] - prices[left]
            
            maxProfit = max(maxProfit, profit)
        
        return maxProfit

                 