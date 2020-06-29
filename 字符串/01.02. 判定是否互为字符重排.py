"""
01.02. 判定是否互为字符重排
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false
说明：

0 <= len(s1) <= 100
0 <= len(s2) <= 100

链接：https://leetcode-cn.com/problems/check-permutation-lcci
"""


class Solution:

    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return set(s2) == set(s1) and len(s1) == len(s2)

    def CheckPermutation2(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        d = {}
        for x, y in zip(s1, s2):
            d[x] = d.get(x, 0) + 1
            d[y] = d.get(y, 0) - 1

        return not any(d.values())


s = Solution()
s1 = "abc"
s2 = "bca"
print(s.CheckPermutation(s1, s2))
print(s.CheckPermutation2(s1, s2))
