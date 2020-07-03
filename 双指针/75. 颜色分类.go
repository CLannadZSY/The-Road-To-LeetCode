/*

*/
package main

import "fmt"

func sortColors(nums []int)  {
    i, j := 0, len(nums) - 1
    step := 0
    for step <= j {
        if nums[step] == 0 {
            nums[i], nums[step] = nums[step], nums[i]
            i++
            step++
        } else if nums[step] == 2 {
            nums[step], nums[j] = nums[j], nums[step]
            j--
        } else {
            step++
        }
    }
    fmt.Println(nums)
}

func main() {
    nums := []int{2,0,2,1,1,0}
    sortColors(nums)
}