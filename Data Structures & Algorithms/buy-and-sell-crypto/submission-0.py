class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lo = prices[0]
        for n in prices:
            maxProfit = max(maxProfit, n - lo)
            if n < lo:lo = n
        return maxProfit