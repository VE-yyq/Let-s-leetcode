# _*_ coding: utf-8 _*_
"""
@Date:       2022/5/8 21:19
@Author:     wz
@File:       有权重有放回背包问题.py
@Decs:
"""


"""
给定一个总数limit，现有[1,2,5,10,20,50,100]的币值大小的货币，不限个数，问有多少种方式凑出共limit

input: values: [1,2,5,10,20,50,100] limit: 5
output: 1/1/1/1/1 1/1/1/2 1/2/2 5 共四种
"""


class Solution:
    """"
     1、该题有 暴力递归 和 动态规划 两种解法。
    """

    def __init__(self, coins):
        self.coins = coins

    def combination(self, limit_price):
        print(self.recursion_combination(limit_price, 0))

    def recursion_combination(self, limit_price, index):
        """
        对硬币类型从左到右暴力穷举
        index 的含义为，当前递归过程讨论的时，对self.coins[index]这个币种
            for循环为取index位置，0次 1次 2次 至超出limit。
            1、base case: 当limit_price为0表示已经凑齐了，直接可以返回1；否则凑到最后超出所有的币种，limit_price都为凑满，则为0
            2、for循环展开：
                对index位置的币种取number次的情况，暴力递归
        """
        if limit_price == 0:
            return 1
        if index == len(self.coins):
            return 0

        ways = 0
        number = 0
        while number * self.coins[index] <= limit_price:
            ways += self.recursion_combination(limit_price - number * self.coins[index], index + 1)
            number += 1
        return ways


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100]
    limit = 100
    s = Solution(coins)
    s.combination(limit)

"""

"""