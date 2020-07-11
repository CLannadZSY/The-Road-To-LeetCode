"""
1447. 最简分数
给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。分数可以以 任意 顺序返回。

 

示例 1：

输入：n = 2
输出：["1/2"]
解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
示例 2：

输入：n = 3
输出：["1/2","1/3","2/3"]
示例 3：

输入：n = 4
输出：["1/2","1/3","1/4","2/3","3/4"]
解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。
示例 4：

输入：n = 1
输出：[]
 

提示：

1 <= n <= 100

链接：https://leetcode-cn.com/problems/simplified-fractions
"""
import math
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ret = []
        if n == 1: return ret
        return [f"{j}/{i}" for i in range(1, n + 1) for j in range(1, i) if j == 1 or math.gcd(i, j) == 1]


s = Solution()
n = 2
print(s.simplifiedFractions(n))



