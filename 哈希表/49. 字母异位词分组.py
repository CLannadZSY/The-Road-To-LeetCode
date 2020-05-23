"""
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

链接：https://leetcode-cn.com/problems/group-anagrams
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())



s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))
