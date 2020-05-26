"""
面试题 17.11. 单词距离
有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

示例：

输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
输出：1
提示：

words.length <= 100000

链接：https://leetcode-cn.com/problems/find-closest-lcci
"""
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:

        t1, t2 = -1, -1
        res = len(words)
        for i in range(res):
            if words[i] == word1:
                t1 = i
            elif words[i] == word2:
                t2 = i

            if t1 != -1 and t2 != -1:
                res = min(res, abs(t1 - t2))
            if res == 1:
                break

        return res




s = Solution()
words = ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"]
word1 = "a"
word2 = "student"

print(s.findClosest(words, word1, word2))
