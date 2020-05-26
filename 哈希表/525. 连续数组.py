"""
525. 连续数组

给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）。

 

示例 1:

输入: [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 

注意: 给定的二进制数组的长度不会超过50000。

链接：https://leetcode-cn.com/problems/contiguous-array
"""
import collections
from typing import List


class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        dic = collections.defaultdict(int)
        count = 0
        dic[count] = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                count -= 1
            else:
                count += 1
            if count in dic:
                res = max(res, i - dic[count])
            else:
                dic[count] = i
        return res

    def findMaxLength2(self, nums: List[int]) -> int:
        dic = {0: 0}
        tmp = 0
        res = 0
        for index, i in enumerate(nums):
            if i == 0:
                tmp -= 1

            else:
                tmp += 1
            if tmp in dic:
                res = max(res, index - dic[tmp] + 1)
            else:
                dic[tmp] = index + 1

        return res


s = Solution()
# nums = [0, 1]  # 2
# nums = [0, 1, 0]  # 2
# nums = [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1]  # 10
nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]  # 2
print(s.findMaxLength(nums))
print(s.findMaxLength2(nums))
