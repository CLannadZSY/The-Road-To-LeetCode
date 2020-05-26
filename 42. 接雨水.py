"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:
src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png"

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

链接：https://leetcode-cn.com/problems/trapping-rain-water

"""
from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        """
        左边遍历加从右边遍历等于总面积加原来图像加雨水数的
        :param height:
        :return:
        """
        ans = 0
        h1 = 0
        h2 = 0
        for i in range(len(height)):
            h1 = max(h1, height[i])
            h2 = max(h2, height[-i - 1])
            ans = ans + h1 + h2 - height[i]
        return ans - len(height) * h1

    def trap2(self, height: List[int]) -> int:
        """
        找出最高点
        分别从两边往最高点遍历：如果下一个数比当前数小，说明可以接到水
        :param height:
        :return:
        """

        if not height or len(height) < 2: return 0
        n = len(height)

        # two pointers
        left_max = height[0]
        right_max = height[n - 1]

        left_pos = 1
        right_pos = n - 2
        res = 0
        while left_pos <= right_pos:
            if left_max < right_max:
                # 处理左边的
                water = left_max - height[left_pos]
                if water > 0:
                    res += water
                left_max = max(left_max, height[left_pos])
                left_pos += 1
            else:
                # 处理右边的
                water = right_max - height[right_pos]
                if water > 0:
                    res += water
                right_max = max(right_max, height[right_pos])
                right_pos -= 1
        return res


s = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1] # 6
height = [2, 0, 2]  # 2
height = [5, 4, 1, 2]  # 1
height = [5, 2, 1, 2, 1, 5]  # 14
height = [4, 2, 0, 3, 2, 5]  # 9
height = [9, 6, 8, 8, 5, 6, 3]  # 3
height = [2, 8, 5, 5, 6, 1, 7, 4, 5]  # 12

print(s.trap(height))
print(s.trap2(height))
