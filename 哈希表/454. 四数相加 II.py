"""
454. 四数相加 II
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

链接：https://leetcode-cn.com/problems/4sum-ii
"""
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        遍历 A 和 B 所有元素和的组合情况，并记录在 ab_map 中，ab_map 的 key 为两数和，value 为该两数和出现的次数
        遍历 C 和 D 所有元素和的组合情况，取和的负值判断其是否在 ab_map 中，若存在则取出 ab_map 对应的 value 值，count = count + value
        """
        count = 0
        ab_map = dict()

        for a in A:
            for b in B:
                ab_map[a + b] = ab_map.get(a + b, 0) + 1

        for c in C:
            for d in D:
                x = -(c + d)
                if x in ab_map:
                    count += ab_map[x]

        return count


s = Solution()
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(s.fourSumCount(A, B, C, D))
