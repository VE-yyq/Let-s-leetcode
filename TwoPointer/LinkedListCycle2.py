# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/8 11:33 上午
@Author:     wz
@File:       LinkedListCycle2.py
@Decs:
"""

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
        '''
        本题用单指针也能实现，用一个list保存已经访问过的node，遍历的退出条件为 1、list内有已经访问过的node或者 2、到达无环链表的末尾
        不过空间复杂为o(N)
        Returns:

        '''
        head = link_list.head
        p = head
        node_list = []
        while p not in node_list and p:
            node_list.append(p)
            p = p.next

        return p


# 初始节点
class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


# 初始化链表
class LinkList:

    def __init__(self, length, array=None):
        self.length = length
        self.head = self.init(array)

    def init(self, array):

        if array and len(array) == self.length:
            flag = True
            head = Node(array[0])
        else:
            flag = False
            head = Node()

        p = head
        for i in range(1, self.length):
            if flag:
                p.next = Node(array[i])
            else:
                p.next = Node()
            p = p.next
        return head


if __name__ == "__main__":

    nums = [1, 2, 3, 4, 5, 6, 7]

    link_list = LinkList(len(nums), nums)
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
