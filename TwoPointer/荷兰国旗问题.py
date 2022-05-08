# _*_ coding: utf-8 _*_
"""
@Date:       2022/1/23 22:49
@Author:     wz
@File:       荷兰国旗问题.py
@Decs:
"""

"""
1. 给定一个数组nums和一个数given，请把小于等于given的数放在数组左边，大于的放在数组右边。空间O(1) 时间O(N)

荷兰国旗问题（因为荷兰国旗三种颜色分别对应'<' '=' '>'）
2. 给定一个数组nums和一个数given，请把小于given的数放在数组左边，等于的放在中间，大于的放在数组右边。空间O(1) 时间O(N)
"""


class Solution:
    """
    解法只进行一次迭代的快排
    对于问题一：
    - 给两个指针，起始位置为0，0，分别标识 小于等于区域的右侧一位 less_or_equal，迭代指针 ptr。ptr遍历数组，有两种情况：
        - ptr指针处小于等于given，less_or_equal位置与ptr位置交换 less_or_equal += 1且ptr += 1
        - ptr指针处大于given，ptr += 1
      ptr指针遍历完成（ while ptr <= len(nums)-1: ）即可

    对于问题二：
    - 给定三个指针，起始位置为0，0，len(nums)-1，分别标识小于区域的右侧一位 less，迭代指针ptr，大于区域左侧一位 greater。迭代有三种情况：
        - ptr指针处小于given，less位置与ptr位置交换 less += 1且ptr += 1
        - ptr指针处等于given，ptr += 1
        - ptr指针处大于given，greater位置与ptr位置交换 greater -= 1  ps:此处ptr不需要加一的原因在于交换过来的greater位置的数字ptr并没有比较过，这也是循环终止条件为啥不需要走到底的原因
      ptr指针进入大于区域 （ while ptr <= greater: ）即可

    问题的解决思路类似于比较过的区域一步步推着未比较的区间，最终完成遍历
    """

    def __init__(self, nums):
        self.nums = nums

    #  双色问题
    def small_big_rank(self, given):
        less_or_equal, ptr = 0, 0
        while ptr < len(self.nums):
            if self.nums[ptr] <= given:
                # if可加可不加，只是可能可以减少几次不需要的原地swap （起效于循环开始时前面正好都是小于等于given的case，但凡有一个大于的，后面都需要交换 鸡肋的要死）
                if less_or_equal != ptr:
                    self.nums[ptr], self.nums[less_or_equal] = self.nums[less_or_equal], self.nums[ptr]
                less_or_equal += 1
            ptr += 1

    #  三色问题
    def small_given_big_rank(self, given):
        less, ptr, greater = 0, 0, len(self.nums) - 1
        while ptr <= greater:
            if self.nums[ptr] < given:
                self.nums[less], self.nums[ptr] = self.nums[ptr], self.nums[less]
                less += 1
                ptr += 1
            elif self.nums[ptr] == given:
                ptr += 1
            elif self.nums[ptr] > given:
                self.nums[greater], self.nums[ptr] = self.nums[ptr], self.nums[greater]
                greater -= 1


if __name__ == "__main__":
    nums = [3, 2, 3, 1, 5, 4, 3, 2]
    s = Solution(nums)
    s.small_big_rank(3)
    print(s.nums)
    s.small_given_big_rank(3)
    print(s.nums)
