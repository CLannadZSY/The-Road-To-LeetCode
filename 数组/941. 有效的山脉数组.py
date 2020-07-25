"""
941. 有效的山脉数组
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

A.length >= 3
在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 
src="https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png"

示例 1：

输入：[2,1]
输出：false
示例 2：

输入：[3,5,5]
输出：false
示例 3：

输入：[0,3,2,1]
输出：true

链接：https://leetcode-cn.com/problems/valid-mountain-array
"""
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

        l = len(A)
        if l < 3: return False

        i, j = 0, l - 1

        while i < j:
            if A[i] <= A[i + 1]:
                i += 1
            else:
                break

        while j > i:
            if A[j] < A[j - 1]:
                j -= 1
            else:
                break

        if i == j and i != 0 and j != l - 1:
            return True

        return False
