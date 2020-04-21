"""
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。


示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/

链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
"""
from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        # if not nums:
        #     return -2 ** 31
        #
        # for i in range(1, len(nums)):
        #     nums[i] = nums[i] + max(nums[i - 1], 0)
        # return max(nums)

        # 更快的写法
        dp = nums
        for idx in range(1, len(dp)):
            if dp[idx - 1] > 0:
                dp[idx] = dp[idx - 1] + nums[idx]
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(num))
