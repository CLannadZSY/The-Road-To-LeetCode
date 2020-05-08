"""
121. 买卖股票的最佳时机

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。


示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minNum, maxNum = max(prices) if prices else 0, 0
        for i in range(len(prices)):
            minNum = min(minNum, prices[i])
            maxNum = max(maxNum, prices[i] - minNum)
        return maxNum

    def maxProfit2(self, prices: List[int]) -> int:
        """
        动态规划
        """
        len_price = len(prices)
        if len(prices) < 2:
            return 0

        # 因为是浅拷贝列表, 会统一改变, 所以导致结果计算错误
        # dp = [[[0] * 2] * 2] * len_price

        # 生成器
        dp = [[[0, 0] for _ in range(2)] for _ in range(len_price)]
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]
        for i in range(1, len_price):
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][1] + prices[i])
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][0][0] - prices[i])

        return dp[-1][1][0]


s = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(prices))
print(s.maxProfit2(prices))
