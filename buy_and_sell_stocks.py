class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_price = prices[0]
        sell_price = 0
        ready_to_sell_prices = [0, 0]
        ready_to_sell = False

        for price in prices:

            if price <= buy_price:
                buy_price = price
                sell_price = 0
                ready_to_sell = False
            else:
                if sell_price <= price:
                    sell_price = price
                    ready_to_sell = True

            if ready_to_sell and (ready_to_sell_prices[1] - ready_to_sell_prices[0]) < (sell_price - buy_price):
                ready_to_sell_prices = [buy_price, sell_price]

        return ready_to_sell_prices[1] - ready_to_sell_prices[0]
