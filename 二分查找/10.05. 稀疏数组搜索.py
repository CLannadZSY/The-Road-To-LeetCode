"""
10.05. 稀疏数组搜索

稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例1:

 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1。
示例2:

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4
提示:

words的长度在[1, 1000000]之间

链接：https://leetcode-cn.com/problems/sparse-array-search-lcci
"""
from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:

        i, j = 0, len(words) - 1
        while i <= j:
            if words[i] == s:
                return i

            if words[j] == s:
                return j

            i += 1
            j -= 1

        return -1


ss = Solution()
words = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
s = "ball"
print(ss.findString(words, s))
