class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_price = prices[0]
        sell_price = 0
        ready_to_sell = False
        total_profit = 0

        for price in prices:
            if buy_price >= price:
                buy_price = price
                ready_to_sell = False
            else:
                sell_price = price
                ready_to_sell = True

            if ready_to_sell:
                total_profit += sell_price - buy_price
                sell_price = 0
                buy_price = price
                ready_to_sell = False

        return total_profit

