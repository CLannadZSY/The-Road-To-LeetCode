"""
287. 寻找重复数
给定一个包含n + 1 个整数的数组nums，其数字都在 1 到 n之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

链接：https://leetcode-cn.com/problems/find-the-duplicate-number
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = dict()
        for n in nums:
            nn = d.get(n, 0)
            if nn > 0:
                return n
            else:
                d[n] = nn + 1
                
    def findDuplicate2(self, nums: List[int]) -> int:
        opt = set()
        for i in nums:
            if i in opt:
                return i
            opt.add(i)


s = Solution()
nums = [1, 3, 4, 2, 2]
print(s.findDuplicate(nums))
print(s.findDuplicate2(nums))
