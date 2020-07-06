"""
1493. 删掉一个元素以后全为 1 的最长子数组

给你一个二进制数组 nums ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。

 

提示 1：

输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：

输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
示例 3：

输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
示例 4：

输入：nums = [1,1,0,0,1,1,1,0,1]
输出：4
示例 5：

输入：nums = [0,0,0]
输出：0
 

提示：

1 <= nums.length <= 10^5
nums[i] 要么是 0 要么是 1 。

链接：https://leetcode-cn.com/problems/longest-subarray-of-1s-after-deleting-one-element
"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        超出时间限制
        :param nums:
        :return:
        """
        if 1 not in nums: return 0

        if len(set(nums)) == 1: return len(nums) - 1

        ret = 0
        l_n = len(nums)
        for i in range(l_n):
            j = i + 1
            max_len = 0
            count = 1
            if nums[i] == 1:
                max_len += 1
            else:
                count -= 1

            while j < l_n:
                if nums[j] == 1:
                    max_len += 1
                else:
                    if count == 0:
                        break
                    count -= 1

                j += 1

            ret = max(max_len, ret)

            if ret == l_n:
                return ret

        return ret

    def longestSubarray2(self, nums: List[int]) -> int:
        """
        动态规划
        :param nums:
        :return: 
        """
        ret, a, b = 0, 0, 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                a += 1
                b += 1
                ret = max(ret, a)
            else:
                a, b = b, 0
        if ret == n: ret -= 1
        return ret



s = Solution()
nums = [0,0,0]
print(s.longestSubarray(nums))
