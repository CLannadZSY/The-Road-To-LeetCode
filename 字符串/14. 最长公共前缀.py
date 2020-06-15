"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

链接：https://leetcode-cn.com/problems/longest-common-prefix
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ''
        for s in zip(*strs):
            if len(set(s)) == 1:
                ret += s[0]
            else:
                return ret
        return ret

ss = Solution()
strs = ["flower","flow","flight"] # fl
print(ss.longestCommonPrefix(strs))