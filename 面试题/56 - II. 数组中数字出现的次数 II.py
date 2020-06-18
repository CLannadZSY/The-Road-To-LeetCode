"""
56 - II. 数组中数字出现的次数 II

在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。



示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1

限制：

1 <= nums.length <= 10000
1 <= nums[i] < 2^31

链接: https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        d = dict()

        for n in nums:
            d[n] = d.get(n, 0) + 1

        for x, y in d.items():
            if y == 1:
                return x
        return 0


s = Solution()
nums = [3, 4, 3, 3]
print(s.singleNumber(nums))
