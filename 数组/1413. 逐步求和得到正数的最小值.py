"""
1413. 逐步求和得到正数的最小值
给你一个整数数组 nums。你可以选定任意的正数 startValue 作为初始值。

你需要从左到右遍历 nums数组，并将 startValue 依次累加上nums数组中的值。

请你在确保累加和始终大于等于 1 的前提下，选出一个最小的正数作为 startValue 。



示例 1：

输入：nums = [-3,2,-3,4,2]
输出：5
解释：如果你选择 startValue = 4，在第三次累加时，和小于 1 。
                累加求和
               startValue = 4 | startValue = 5 | nums
                 (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                 (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                 (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                 (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                 (4 +2 ) = 6  | (5 +2 ) = 7    |   2
示例 2：

输入：nums = [1,2]
输出：1
解释：最小的 startValue 需要是正数。
示例 3：

输入：nums = [1,-2,-3]
输出：5


提示：

1 <= nums.length <= 100
-100 <= nums[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        nums[:] = nums[::-1]

        nn = []
        for i, n in enumerate(nums):
            if n < 0:
                nn = nums[i:]
                break

        ss = sum(nn)
        return abs(ss) + 1 if ss < 0 else 1


s = Solution()
nums = [-3, 2, -3, 4, 2]  # 5
nums = [2, 3, 5, -5, -1]  # 1
nums = [-5, -2, 4, 4, -2]  # 8

print(s.minStartValue(nums))
