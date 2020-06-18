"""
40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
"""
import heapq
import random
from typing import List


class Solution:

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """
        时间复杂度：O(n\log n)O(nlogn)，其中 nn 是数组 arr 的长度。算法的时间复杂度即排序的时间复杂度。
        空间复杂度：O(\log n)O(logn)，排序所需额外的空间复杂度为 O(\log n)O(logn)。

        :param arr:
        :param k:
        :return:
        """
        arr = sorted(arr)
        return arr[:k]

    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        """
        堆
        时间复杂度：O(n\log k)O(nlogk)，其中 nn 是数组 arr 的长度。由于大根堆实时维护前 kk 小值，所以插入删除都是 O(\log k)O(logk) 的时间复杂度，最坏情况下数组里 nn 个数都会插入，所以一共需要 O(n\log k)O(nlogk) 的时间复杂度。

        空间复杂度：O(k)O(k)，因为大根堆里最多 kk 个数。

        :param arr:
        :param k:
        :return:
        """
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


class Solution2:
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def randomized_selected(self, arr, l, r, k):
        pos = self.randomized_partition(arr, l, r)
        num = pos - l + 1
        if k < num:
            self.randomized_selected(arr, l, pos - 1, k)
        elif k > num:
            self.randomized_selected(arr, pos + 1, r, k - num)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        self.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]


s = Solution()
arr = [2, 1, 3, 6, 5, 4]
k = 3
print(s.getLeastNumbers(arr, k))
print(s.getLeastNumbers2(arr, k))

ss = Solution2()
print(ss.getLeastNumbers(arr, k))
