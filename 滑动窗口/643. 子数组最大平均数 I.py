"""
643. 子数组最大平均数 I
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。



示例：

输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75


提示：

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-average-subarray-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random
from typing import List

from comm import func_time


class Solution:

    @func_time
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        滑动窗口
        """
        i, j = 0, k
        x = sum(nums[i:j])
        res = x

        while j < len(nums):
            x = x - nums[i] + nums[j]

            res = max(res, x)
            i += 1
            j += 1

        return res / k


if __name__ == '__main__':
    S = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    nums = [4, 0, 4, 3, 3]
    k = 5

    nums = [random.randint(-10000, 10000) for _ in range(100000)]
    k = 10
    print(S.findMaxAverage(nums, k))
