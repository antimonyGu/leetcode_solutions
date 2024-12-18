class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            # buy stock in min price
            buy_price = min(buy_price, p)
            # update max profit
            profit = max(profit, p - buy_price)

        return profit