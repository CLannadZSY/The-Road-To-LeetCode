/*
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

链接：https://leetcode-cn.com/problems/longest-common-prefix
*/
package main

import "fmt"

func longestCommonPrefix(strs []string) string {
    if len(strs) == 0 {
		return ""
	}
	for i := 0; i < len(strs[0]); i++ {
		for j := 1; j < len(strs); j++ {
			if i == len(strs[j]) || strs[j][i] != strs[0][i] {
				return strs[0][:i]
			}
		}
	}
	return strs[0]

}

func longestCommonPrefix2(strs []string) string {
	if len(strs) == 0 {
        return ""
    }
    // 以列表第一个字符串为基准字符串， 逐一判断每一个字符
    for index, char := range strs[0] {
        // 根据基准字符串对比列表中其他字符串相同位置字符是否相等
        for _, v := range strs {
            // 如果index大于当前字符串长度，直接返回当前字符串。不可能还有更长的公共前缀
            if index >= len(v) {
                return v
            }
            // 如果当前字符串不相等，说明前面的是已经匹配上的
            if v[index] != byte(char) {
                return v[:index]
            }
        }
    }
    return strs[0]

}

func main() {
    strs := []string{"flower","flow","flight"}
    fmt.Println(longestCommonPrefix(strs))
    fmt.Println(longestCommonPrefix2(strs))
}