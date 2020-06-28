/*
10.05. 稀疏数组搜索

稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例1:

 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1。
示例2:

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4
提示:

words的长度在[1, 1000000]之间

链接：https://leetcode-cn.com/problems/sparse-array-search-lcci
*/
package main

import "fmt"

func findString(words []string, s string) int {

	i, j := 0, len(words)-1
	for i <= j {
		if words[i] == s {
			return i
		}
		if words[j] == s {
			return j
		}
		i++
		j--
	}
	return -1
}

func main() {
	words := []string{"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
	s := "ball"
	fmt.Println(findString(words, s))
}
