"""
1539. 第 k 个缺失的正整数
给你一个 严格升序排列的正整数数组 arr和一个整数k。

请你找到这个数组里第k个缺失的正整数。



示例 1：

输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
示例 2：

输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。


提示：

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
对于所有1 <= i < j <= arr.length的 i和 j 满足arr[i] < arr[j]

链接：https://leetcode-cn.com/problems/kth-missing-positive-number
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        ret = 0
        c = 0
        while c < k:
            ret += 1
            if ret not in arr:
                c += 1
        return ret
