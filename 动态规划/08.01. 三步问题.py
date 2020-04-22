"""
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，
计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间

链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
"""


class Solution:
    def waysToStep(self, n: int) -> int:
        # 递归太慢, 肯定不能用
        # if n <= 1:
        #     return 1
        # if n == 2:
        #     return 2
        #
        # return self.waysToStep(n - 1) + self.waysToStep(n - 2) + self.waysToStep(n - 3)

        # 第 N 项 = [N - 3, N) 项和

        dp = {
            0: 1,
            1: 1,
            2: 2,
            3: 4
        }

        if n in dp:
            return dp[n]

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007

        return dp[n]

    def waysToStep2(self, n: int) -> int:

        if n <= 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            a1, a2, a3 = 1, 2, 4
            for i in range(3, n):
                ans = (a1 + a2 + a3) % 1000000007
                a1, a2, a3 = a2, a3, ans
            return ans


s = Solution()
n = 7
print(s.waysToStep(n))
print(s.waysToStep2(n))
