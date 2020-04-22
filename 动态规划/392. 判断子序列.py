"""
392. 判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.

后续挑战 :

如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

链接: https://leetcode-cn.com/problems/is-subsequence/
"""
import copy


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        len_t = len(t)
        last_i = 0
        for m in s:
            # 不能每次都扫描所有, 而是记录上次位置
            for i in range(last_i, len_t):
                if t[i] == m:
                    last_i = i + 1
                    break
            else:
                return False

        return True

    def isSubsequence2(self, s: str, t: str) -> bool:

        l = -1
        for i in s:
            l = t.find(i, l + 1)
            if l == -1:
                return False
        return True

    def isSubsequence3(self, s: str, t: str) -> bool:

        t = iter(t)
        return all(i in t for i in s)


sl = Solution()
s = "abc"
t = "ahbgdc"

print(sl.isSubsequence(s, t))
print(sl.isSubsequence2(s, t))
print(sl.isSubsequence3(s, t))
