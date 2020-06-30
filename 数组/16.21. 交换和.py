"""
面试题 16.21. 交换和
给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。

返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。

示例:

输入: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
输出: [1, 3]
示例:

输入: array1 = [1, 2, 3], array2 = [4, 5, 6]
输出: []
提示：

1 <= array1.length, array2.length <= 100000

链接：https://leetcode-cn.com/problems/sum-swap-lcci
"""
from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum_array1 = sum(array1)
        sum_array2 = sum(array2)

        # 两数组和之差必须为偶数,才可能交换
        if (sum_array1 - sum_array2) % 2:
            return []

        diff = (sum_array1 - sum_array2) // 2
        array2 = set(array2)

        for num in array1:
            if num - diff in array2:
                return [num, num - diff]
        return []


s = Solution()
array1 = [4, 1, 2, 1, 1, 2]
array2 = [3, 6, 3, 3]
print(s.findSwapValues(array1, array2))
