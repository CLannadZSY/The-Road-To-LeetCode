"""
714. 买卖股票的最佳时机含手续费

给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        动态规划
        """
        len_prices = len(prices)
        if len_prices < 2:
            return 0

        dp = [[0, 0] for _ in range(len_prices)]
        dp[0][1] = -prices[0]
        for i in range(1, len_prices):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]

    def maxProfit2(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        unhold, hold = 0, -float("inf")
        print(f'price=0, {unhold=}, {hold=}')
        for price in prices:
            # 不持有股票时的最大利润
            # 可以保持不变，或者卖出这一天的股票
            unhold = max(unhold, hold + price - fee)

            # 持有股票时的最大利润
            # 可以保持不变，或者买入这一天的股票
            hold = max(hold, unhold - price)
            print(f'{price=}, {unhold=}, {hold=}')
        return unhold


s = Solution()
prices = [1, 4, 7, 2, 5, 8]  # 8
fee = 2
print(s.maxProfit(prices, fee))
print(s.maxProfit2(prices, fee))
