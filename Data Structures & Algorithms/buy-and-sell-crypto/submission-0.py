class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        while i < (len(prices)-1):
            s = max(prices[i:])
            current = s - prices[i]
            profit = max(profit,current)
            i += 1
        return profit
            

