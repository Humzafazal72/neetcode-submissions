class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0

        for i in range(1,len(prices)):
            if prices[buy]>prices[i]:
                buy = i
                continue
            else:
                profit  = prices[i] - prices[buy]
                max_profit = profit if profit>max_profit else max_profit
        
        return max_profit