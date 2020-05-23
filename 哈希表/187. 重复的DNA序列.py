"""
187. 重复的DNA序列

所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找子串，这个子串长度为10，在原字符串中出现超过一次。 的序列（子串）。

 

示例：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]

链接：https://leetcode-cn.com/problems/repeated-dna-sequences
"""
from typing import List


class Solution:

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        d = dict()
        for i, _ in enumerate(s[:-9]):
            x = s[i: i + 10]
            d[x] = d.get(x, 0) + 1

        ret = [x[0] for x in (filter(lambda x: x[1] > 1, d.items()))]
        return ret

    def findRepeatedDnaSequences2(self, s: str) -> List[str]:
        L, n = 10, len(s)
        seen, output = set(), set()

        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return list(output)


s = Solution()
ss = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
print(s.findRepeatedDnaSequences(ss))
print(s.findRepeatedDnaSequences2(ss))
