# _*_ coding: utf-8 _*_
"""
@Date:       2022/1/17 0:28
@Author:     wz
@File:       memory.py
@Decs:
"""


def memory_test(arr):
    arr[1] = 3


def arr_max(arr, left, right):
    if left == right:
        return arr[left]

    mid = (right - left) // 2 + left
    left_max = arr_max(arr, left, mid)
    right_max = arr_max(arr, mid + 1, right)
    return max(left_max, right_max)

arr = [1, 2]
memory_test(arr)
print(arr)
maximums = arr_max(arr, 0, len(arr) - 1)
print(maximums)
