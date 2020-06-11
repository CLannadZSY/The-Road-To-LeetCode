/*
739. 每日温度
请根据每日 气温 列表，重新生成一个列表，对应位置的输出是需要再等待多少天才能等到一个更高的气温。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

链接：https://leetcode-cn.com/problems/daily-temperatures
*/

package main

import "fmt"

func dailyTemperatures(T []int) []int {
    length := len(T)
    ans := make([]int, length)
    stack := []int{}
    for i := 0; i < length; i++ {
        temperature := T[i]
        for len(stack) > 0 && temperature > T[stack[len(stack)-1]] {
            prevIndex := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            ans[prevIndex] = i - prevIndex
        }
        stack = append(stack, i)
    }
    return ans

}

func dailyTemperatures2(T []int) []int {

	R := make([]int, len(T))
	stack := []int{}

	for k, v := range T {
		for len(stack) > 0 && T[stack[len(stack)-1]] < v {
			i := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			R[i] = k - i
		}
		stack = append(stack, k)
	}
	return R
}

func main {
    temperatures := int[]{73, 74, 75, 71, 69, 72, 76, 73}
    ret := dailyTemperatures(temperatures)
    fmt.Println(ret)
    ret := dailyTemperatures2(temperatures)
    fmt.Println(ret)
}