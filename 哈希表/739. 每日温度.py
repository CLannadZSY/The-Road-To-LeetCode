"""
739. 每日温度

请根据每日 气温 列表，重新生成一个列表，对应位置的输出是需要再等待多少天才能等到一个更高的气温。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

链接：https://leetcode-cn.com/problems/daily-temperatures

"""
from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
            单调栈
        :return:
        """
        stack = list()
        t_length = len(T)
        res_list = [0 for _ in range(t_length)]

        for key, value in enumerate(T):
            if stack:
                while stack and T[stack[-1]] < value:
                    res_list[stack[-1]] = key - stack[-1]
                    stack.pop()
            stack.append(key)
        return res_list

    def dailyTemperatures2(self, T: List[int]) -> List[int]:
        """
            暴力解法
        :return:
        """
        n = len(T)
        ans, nxt, big = [0] * n, dict(), 10 ** 9
        for i in range(n - 1, -1, -1):
            warmer_index = min(nxt.get(t, big) for t in range(T[i] + 1, 102))
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans



s = Solution()
t = [73, 74, 75, 71, 69, 72, 76, 73]  # [1, 1, 4, 2, 1, 1, 0, 0]
print(s.dailyTemperatures(t))
print(s.dailyTemperatures2(t))
