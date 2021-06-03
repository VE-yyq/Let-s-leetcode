# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/23 4:51 下午
@Author:     wz
@File:       FindFirstAndLastPositionOfElement.py
@Decs:
"""


'''
题目描述

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''



class Solution():

    def first_and_last_position(self, nums, target):
        '''
        很典型的一道二分查找。
        通过查找过程中，当满足查找条件时，通过控制是left还是right进行移动，来控制查找区间，从而找到区间内符合查找条件最开始和最末尾位置。
        Args:
            nums:

        Returns:

        '''

        if not nums:
            return [-1, -1]

        first = self.first_equal_position(nums, target)
        last = self.last_equal_position(nums, target)
        print(first, last)

        # 这里两个判断条件（短路或）
        #   1、first == len(nums) 一个是为了解决nums=[1] target=4这类情况
        #   2、nums[first] != target 是为了解决较为多发的nums=[1,2,2,4] target=3这类本身就找不到的情况
        if first == len(nums) or nums[first] != target: # 当然也可以用last来判断 last == -1 or nums[last] != target
            return [-1, -1]

        return [first, last]


    def first_equal_position(self, nums, target):

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else: # 当相等时，继续往左侧寻找，看是否还有相等的情况
                right = mid - 1
        return left # 模拟一下就知道为啥最终返回left


    def last_equal_position(self, nums, target):

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else: # 当相等时，继续往右侧寻找，看是否还有相等的情况
                left = mid + 1
        return right # 模拟一下就知道为啥最终返回right


if __name__ == "__main__":

    nums = [9]
    target = 4

    solution = Solution()
    print(solution.first_and_last_position(nums, target))