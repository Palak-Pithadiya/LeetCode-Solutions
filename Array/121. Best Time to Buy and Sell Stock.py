class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
            
        min_profit = prices[0]
        max_profit = 0

        for num in prices:
            min_profit = min(min_profit, num)
            max_profit = max(max_profit, num - min_profit)

        return max_profit
