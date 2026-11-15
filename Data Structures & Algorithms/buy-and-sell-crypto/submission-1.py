class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        left = 0

        for right in range(n):

            profit = prices[right] - prices[left]

            while prices[left] > prices[right]:
                left += 1
            
            maxProfit = max(maxProfit, profit)
        
        return maxProfit

                 