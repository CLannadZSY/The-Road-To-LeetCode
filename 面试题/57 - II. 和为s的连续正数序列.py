"""
57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5

链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
"""
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """滑动窗口"""
        i = 1
        j = 1
        sum = 0
        res = []

        while i <= target // 2:
            if sum < target:
                sum += j
                j += 1
            elif sum > target:
                sum -= i
                i += 1
            else:
                arr = list(range(i, j))
                res.append(arr)
                sum -= i
                i += 1

        return res


s = Solution()
target = 10
print(s.findContinuousSequence(target))
