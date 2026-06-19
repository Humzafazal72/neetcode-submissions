class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s,e = 0,1
        max_profit = 0

        while(s<len(prices)-1 and e<=len(prices)-1):
            profit = prices[e]-prices[s]
            if profit< max_profit:
                if prices[e]<prices[s]:
                    s = s + 1
                    e = s + 1  
                    continue                  
            else:
                max_profit = profit
            e =  e + 1 

        return max_profit


        