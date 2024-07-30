class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy,sell = 0,1

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if prices[sell] < prices[buy]:
                buy = sell
            maxProfit = max(profit,maxProfit)
            sell += 1
        return maxProfit
             