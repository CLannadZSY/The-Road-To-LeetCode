/*
345. 反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
且字符串包含大小写字母(自己添加, 垃圾官方)


示例 1：

输入："hello"
输出："holle"
示例 2：

输入："leetcode"
输出："leotcede"


提示：

元音字母不包含字母 "y" 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "leetcode"
	fmt.Println(reverseVowels(s))
}

func reverseVowels(s string) string {
	vowelChar := "aoeiuAOEIU"
	t := []byte(s)
	n := len(t)
	i, j := 0, n-1
	for i < j {
		for i < n && !strings.Contains(vowelChar, string(t[i])) {
			i++
		}
		for j > 0 && !strings.Contains(vowelChar, string(t[j])) {
			j--
		}
		if i < j {
			t[i], t[j] = t[j], t[i]
			i++
			j--
		}
	}
	return string(t)

}
