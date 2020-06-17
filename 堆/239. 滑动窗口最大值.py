"""
239. 滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。


进阶：

你能在线性时间复杂度内解决此题吗？


示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

链接：https://leetcode-cn.com/problems/sliding-window-maximum
"""
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        524 ms
        :param nums:
        :param k:
        :return:
        """
        ret = []

        temp_num = nums[:k]
        mx_val = max(temp_num)
        mx_index = temp_num.index(mx_val)
        ret.append(mx_val)

        for i in range(1, len(nums) - k + 1):
            temp_num.pop(0)
            temp_num.append(nums[i + k - 1])

            if mx_index > 0:
                mx_val = max(mx_val, nums[i + k - 1])
                mx_index -= 1
            else:
                mx_val = max(temp_num)
                mx_index = temp_num.index(mx_val)

            ret.append(mx_val)

        return ret


s = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(s.maxSlidingWindow(nums, k))
