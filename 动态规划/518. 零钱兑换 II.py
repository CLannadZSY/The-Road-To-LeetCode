"""
518. 零钱兑换 II
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

 

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10]
输出: 1
 

注意:

你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数

链接：https://leetcode-cn.com/problems/coin-change-2
"""
from typing import List


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range((amount + 1))] for _ in range((n + 1))]
        for i in range(n):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if (j - coins[i - 1]) >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][amount]

    def change2(self, amount: int, coins: List[int]) -> int:
        """
        dp 数组的转移只和 dp[i][..] 和 dp[i-1][..] 有关，
        所以可以压缩状态，进一步降低算法的空间复杂度
        """

        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j - coins[i]]
        return dp[amount]

    def change3(self, amount: int, coins: List[int]) -> int:
        """
        官方解法
        时间复杂度：O (N x amount) 其中 N 为 coins 数组的长度
        空间复杂度：O (amount) dp 数组使用的空间。

        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


s = Solution()
amount = 10
coins = [1, 2, 5]
print(s.change(amount, coins))
print(s.change2(amount, coins))
print(s.change3(amount, coins))
