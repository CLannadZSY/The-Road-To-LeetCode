/*
496. 下一个更大元素 I
给你两个 没有重复元素 的数组nums1 和nums2，其中nums1是nums2的子集。

请你找出 nums1中每个元素在nums2中的下一个比其大的值。

nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素。如果不存在，对应位置输出 -1 。



示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
示例 2:

输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
   对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。


提示：

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
nums1和nums2中所有整数 互不相同
nums1 中的所有整数同样出现在 nums2 中

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

// 暴力如我
func nextGreaterElement(nums1 []int, nums2 []int) []int {

	l1 := len(nums1)
	l2 := len(nums2)
	res := make([]int, l1)

	for x, v := range nums1 {
		res[x] = -1

		i := 0
		for v != nums2[i] {
			i++
		}

		if i == l2-1 {
			continue
		}

		for j := i + 1; j < l2; j++ {
			if nums2[j] > v {
				res[x] = nums2[j]
				break
			}
		}
	}
	return res

}

// hash + stack
func nextGreaterElement(nums1 []int, nums2 []int) []int {
	hash := make(map[int]int, len(nums2))
	var stack []int
	for _, num := range nums2 {
		for len(stack) > 0 && stack[len(stack)-1] <= num {
			stackTop := stack[len(stack)-1]
			hash[stackTop] = num
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, num)
	}

	res := make([]int, 0, len(nums1))
	for _, num := range nums1 {
		if value, ok := hash[num]; ok {
			res = append(res, value)
		} else {
			res = append(res, -1)
		}

	}

	return res
}
