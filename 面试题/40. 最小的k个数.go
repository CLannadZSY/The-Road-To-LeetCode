/*
40. 最小的k个数

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。



示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

链接: https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
*/
package main

import (
	"fmt"
	"sort"
)

func getLeastNumbers(arr []int, k int) []int {
	sort.Ints(arr)
	return arr[:min(k, len(arr))]
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	arr := []int{3, 2, 1}
	k := 2
	fmt.Println(getLeastNumbers(arr, k))
}
