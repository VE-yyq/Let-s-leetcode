# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/8 11:33 上午
@Author:     wz
@File:       LinkedListCycle2.py
@Decs:
"""

from LinkedList.LinkedList import LinkedList


'''
题目描述
给定一个链表，如果有环路，找出环路的开始点。

输入输出样例
输入是一个链表，输出是链表的一个节点。如果没有环路，返回一个空指针。
'''


class Solution:

    def link_list_cycle_pointer(self, link_list):
        """
        本题用单指针也能实现，用一个list保存已经访问过的node，遍历的退出条件为 1、list内有已经访问过的node或者 2、到达无环链表的末尾
        不过空间复杂为o(N)
        Returns:

        """
        head = link_list.head
        p = head
        node_list = []
        while p not in node_list and p:
            node_list.append(p)
            p = p.next

        return p

    def link_list_cycle_two_pointer(self, link_list):
        """
        本题用单指针也能实现，用一个list保存已经访问过的node，遍历的退出条件为 1、list内有已经访问过的node或者 2、到达无环链表的末尾
        不过空间复杂为o(N)
        Returns:

        """
        head = link_list.head
        p = head
        node_list = []
        while p not in node_list and p:
            node_list.append(p)
            p = p.next

        return p


if __name__ == "__main__":

    nums = [1, 2, 3, 4, 5, 6, 7]

    link_list = LinkedList(nums)
    print(link_list)
    # 为linkList构建环
    head = link_list.head
    p = head
    while p.next:
        p = p.next

    p.next = head.next.next
    print("-----------")
    print("进入环的节点值：", p.next.value)
    solution = Solution()
    print("单指针算法给出的环的节点值：", solution.link_list_cycle_pointer(link_list).value)
    print("双指针算法给出的环的节点值：", solution.link_list_cycle_two_pointer(link_list).value)
