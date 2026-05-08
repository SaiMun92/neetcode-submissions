class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Use a sliding window technique to find out"""
        current_max = 0
        for i in range(len(prices) - 1):
            j = 1
            while i+j < len(prices):
                buy = prices[i]
                sell = prices[i+j]
                res = sell - buy
                if res > 0 and res > current_max:
                    current_max = res
                j += 1
        return current_max
        