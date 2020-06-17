/*
57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。



示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]


限制：

1 <= target <= 10^5

链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
*/
package main

import "fmt"

func findContinuousSequence(target int) [][]int {
	// 滑动窗口
	i, j := 1, 1
	sum := 0
	var ret = [][]int{}

	for i <= target/2 {
		if sum < target {
			sum += j
			j++
		} else if sum > target {
			sum -= i
			i++
		} else {
			arr := GenNumList(i, j)
			ret = append(ret, arr)
			sum -= i
			i++
		}
	}
	return ret
}

func GenNumList(x, y int) []int {
	ret := []int{}
	for i := x; i < y; i++ {
		ret = append(ret, i)
	}
	return ret
}

func findContinuousSequence2(target int) [][]int {
	// 数学公式法
	left := 1
	right := 2
	ret := [][]int{}
	if target < 3 {
		return ret
	}
	for left < right {
		sum := (left + right) * (right - left + 1) / 2
		if sum == target {
			temp := []int{}
			for i := left; i <= right; i++ {
				temp = append(temp, i)
			}
			ret = append(ret, temp)
			left++
		} else if sum < target {
			right++
		} else if sum > target {
			left++
		}
	}
	return ret
}

func main() {
	target := 9
	fmt.Println(findContinuousSequence(target))
	fmt.Println(findContinuousSequence2(target))
}
