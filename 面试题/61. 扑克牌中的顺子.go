/*
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
 

限制：

数组长度为 5 

数组的数取值为 [0, 13] .

链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
*/
package main

import (
    "sort"
    "fmt"
)

func isStraight(nums []int) bool {
	joker := 0
	sort.Ints(nums)
	for i := 0; i < 4; i++ {
		if nums[i] == 0 {
			joker++
		} else if nums[i] == nums[i+1] {
			return false
		}
	}
	return nums[4]-nums[joker] < 5
}

func main() {
    nums := []int{1, 2, 3, 4, 5}
	fmt.Println(isStraight(nums))
}