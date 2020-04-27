class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')
        i = 0
        while (i < len(prices)):
            if (prices[i] < minPrice):
                minPrice = prices[i]
            elif (prices[i] - minPrice > maxProfit):
                maxProfit = prices[i] - minPrice
            i += 1
        return maxProfit
