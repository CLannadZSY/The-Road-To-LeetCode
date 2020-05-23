"""
451. 根据字符出现频率排序
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
示例 2:

输入:
"cccaaa"

输出:
"cccaaa"

解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
示例 3:

输入:
"Aabb"

输出:
"bbAa"

解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。

链接：https://leetcode-cn.com/problems/sort-characters-by-frequency
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for ss in s:
            d[ss] = d.get(ss, 0) + 1

        return ''.join([m * int(n) for m, n in sorted(d.items(), key=lambda x: x[1], reverse=True)])

    def frequencySort2(self, s: str) -> str:
        from collections import Counter
        s_cnt = Counter(s).most_common()
        res = ""
        for k_v in s_cnt:
            res += k_v[0]*k_v[1]
        return res


x = Solution()
s = 'tree'
print(x.frequencySort(s))
print(x.frequencySort2(s))