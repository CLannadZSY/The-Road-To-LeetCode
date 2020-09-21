import time
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9 --> [3,3] --> 无穷多

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i

if __name__ == '__main__':
    start = time.clock()
    x = Solution()
    print(x.twoSum([2, 7, 11, 15], 26))
    end = time.clock()
    print('运行时间: ', end - start)

