# _*_ coding: utf-8 _*_
"""
@Date:       2022/4/21 0:12
@Author:     wz
@File:       求连续子序列最大和.py
@Decs:
"""

"""
给定一列表，求其连续子序列中，和最大的值

eg：[-1, 3, -2, 5, -2, 3, 4] 最大字串为[3, -2, 5, -2, 3, 4]，最大和为11
"""


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def sub_list_max_sum(self):
        # 初始化dp数组，其中元素dp[i]实际意义为，以i为结束元素的连续子序列其 和的最大值
        dp = [None] * len(self.nums)

        # 初始化dp[0]
        dp[0] = self.nums[0]

        # dp过程
        for i in range(1, len(self.nums)):
            # 状态转移方程的意义，以i为结束元素的连续子序列和的最大值，分为两种情况：1、nums[i]元素另立山头，则dp[i]就等于nums[i]
            #     2、nums[i]元素和前面的子序列形成合力，构成和最大，则dp[i] = dp[i-1] + nums[i]，为啥呢？仔细想想
            #       -> 原因：不妨假设dp[i-1] = nums[i-1-3]+nums[i-1-2]+nums[i-1-1]+nums[i-1]四个数字，此时想要dp[i]最大，且包含nums[i]，
            #               因为nums[i]已经是确定了，所以想要 sth + nums[i]最大，那必然只能是dp[i]，因为dp[i]的定义就是以i为结束元素的连续子序列其 和的最大值
            dp[i] = max(dp[i - 1] + self.nums[i], self.nums[i])

        print(dp)


if __name__ == "__main__":
    nums = [-1, 3, -2, 5, -2, 3, -4]
    s = Solution(nums)
    s.sub_list_max_sum()
