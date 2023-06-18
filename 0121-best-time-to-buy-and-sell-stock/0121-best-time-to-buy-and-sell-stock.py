class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_price = prices[0]
        
        for idx, price in enumerate(prices):

            if price < min_price: # will never be a profit (set new low)
                min_price = price

            elif price - min_price > max_profit: # test delta vs max profit so far
                max_profit = price - min_price

        return max_profit