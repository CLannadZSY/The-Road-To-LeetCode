/*
面试题 17.10. 主要元素
数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。

 

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5
示例 2：

输入：[3,2]
输出：-1
示例 3：

输入：[2,2,1,1,1,2,2]
输出：2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-majority-element-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

package main

import "fmt"

func main() {
	nums := []int{6,5,5}
	fmt.Println(majorityElement(nums))
}

func majorityElement(nums []int) int {

	d := map[int]int{}
	for _, v := range nums {
		if _, ok := d[v]; ok {
			d[v]++
		} else {
			d[v] = 1
		}
	}


	l := len(nums) / 2 + 1

	for x, y := range d {
		if y >=	l {
			return x
		}
	}

	return -1
}
