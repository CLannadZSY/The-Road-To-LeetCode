/*
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
*/
package main

import "fmt"

func maxSlidingWindow(nums []int, k int) []int {
    // 1664 ms 太慢了, 暴力解法
    var ret = []int{}
    for i := 0; i < len(nums) - k + 1; i++ {
        temp_num := nums[i: i + k]
        mx_val := max(temp_num)
        ret = append(ret, mx_val)
    }
    return ret
}

func max(N []int) int {
    maxVal := N[0]
	for i := 1; i < len(N); i++ {
		if maxVal < N[i] {
			maxVal = N[i]
		}
	}
    return maxVal
}

func main() {
    nums := []int{1, 3, -1, -3, 5, 3, 6, 7}
    k := 3
    fmt.Println(maxSlidingWindow(nums, k))
}

