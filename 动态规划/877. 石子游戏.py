"""
877. 石子游戏
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。
这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。


示例：

输入：[5,3,4,5]
输出：true
解释：
亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
 

提示：

2 <= piles.length <= 500
piles.length 是偶数。
1 <= piles[i] <= 500
sum(piles) 是奇数。

链接：https://leetcode-cn.com/problems/stone-game
"""
from functools import lru_cache
from typing import List


class Solution:
    """
    二叉树问题??

    只能从`开始` 或 `结束` 的地方取走石头
    """

    def stoneGame(self, piles: List[int]) -> bool:

        p_len = len(piles)
        if p_len == 2:
            return piles[0] != piles[-1]

        person_one = 0
        person_two = 0
        while True:

            if piles[0] >= piles[-1]:
                person_one += piles[0]
                piles.pop(0)
            else:
                person_one += piles[-1]
                piles.pop(-1)

            if piles[0] <= piles[-1]:
                person_two += piles[0]
                piles.pop(0)
            else:
                person_two += piles[-1]
                piles.pop(-1)

            if not piles:
                return person_one >= person_two

    def stoneGame2(self, piles):
        """
        动态规划
        :param piles:
        :return:
        """
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        return dp(0, N - 1) > 0


s = Solution()
piles = [5, 3, 4, 5, 5, 6, 7, 8, 9, 5, 42, 2, 3, 4, 56, 7, 8, 5, 3, 1]
print(s.stoneGame(piles))
piles = [5, 3, 4, 5, 5, 6, 7, 8, 9, 5, 42, 2, 3, 4, 56, 7, 8, 5, 3, 1]
print(s.stoneGame2(piles))
