class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        an = 0
        l,r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            an = max(profit, an)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return an