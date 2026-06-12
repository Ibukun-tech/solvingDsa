class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r= 0, 1
        maxProfe=0
        while r < len(prices):
            if prices[r]>prices[l]:
                maxProfe= max(maxProfe, prices[r]-prices[l])
            else:
                l=r
            r+=1
        return maxProfe    