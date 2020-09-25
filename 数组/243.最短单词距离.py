"""
243.最短单词距离
描述
给出一系列单词 words，以及两个不同的单词 wordA 和 wordB，请找出最近的两个 wordA 和 wordB 的间距。
如果 words 中不存在 wordA 或 wordB，那么返回 -1

单词只包含大写或小写英文字符。

您在真实的面试中是否遇到过这个题？
说明
样例中，第一个 "hello" 和第一个 "world" 的间距为 11,
但第一个 "world" 和第二个 "hello" 的间距为 22, 所以最后的答案应该是 11.

样例
输入：
["hello","world","say","hello"]
"hello"
"world"
输出：1

链接: https://www.lintcode.com/problem/word-spacing/description

"""
from typing import List


class Solution:

    def wordSpacing(self, words, wordA, wordB):
        if (wordA not in words) or (wordB not in words):
            return -1

        d = dict()
        ret = len(words)
        for i, w in enumerate(words):
            if w in d:
                d[w] += [i]
            else:
                d[w] = [i]

        for i in d[wordA]:
            for j in d[wordB]:
                ret = min(ret, abs(j - i))

        return ret


s = Solution()
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "practice"
word2 = "perfect"
print(s.wordSpacing(words, word1, word2))
