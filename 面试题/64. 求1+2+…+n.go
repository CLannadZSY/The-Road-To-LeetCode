/*
面试题64. 求1+2+…+n
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。



示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45


限制：

1 <= n <= 10000

链接：https://leetcode-cn.com/problems/qiu-12n-lcof
*/
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(sumNums(10))
}

func sumNums(n int) int {
	return (int(math.Pow(float64(n), 2)) + n) >> 1
}
