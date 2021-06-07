"2021/6/7"
import math


class MinStack:
    def __init__(self):
        # 在每个元素a入栈时把当前栈的最小值m存储起来，为此可以使用一个辅助栈，与元素栈同步插入与删除
        self.stack = []
        self.Minstack = [math.inf]  # 注意初始不是空，因为push操作需要对比push元素和初始最小元素

    def push(self, x):
        self.stack.append(x)
        self.Minstack.append(min(x, self.Minstack[-1]))

    def pop(self):
        self.stack.pop()
        self.Minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.Minstack[-1]


'''时间复杂度：题目中所有操作，时间复杂度均为O(1)。因为栈的插入、删除与读取操作都是O(1),定义的每个操作最多调用栈操作两次。
   空间复杂度：O(n)，其中n为总操作数。最坏情况下，我们会连续插入n个元素，此时两个栈占用空间为O(n)
   拓展：不使用额外空间的做法'''


# 这里是拓展问题的解法:栈里保存差值
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_value = -1

    def push(self, x):
        if not self.stack:  # 如果栈空
            self.stack.append(0)  # 初始差值0
            self.min_value = x #最小值存储为新加入元素
        else:
            diff = x - self.min_value #如果栈不为空。计算新加入元素和最小值的差值。
            self.stack.append(diff) #栈内增加差值元素
            self.min_value = self.min_value if diff > 0 else x  # min_value始终保存原始最小值与x之间比较后的最小值

    def pop(self):
        if self.stack:#如果栈内有元素
            diff = self.stack.pop()
            if diff < 0:
                top = self.min_value
                self.min_value = top - diff
            else:
                top = self.min_value + diff
            return top

    def top(self):
        return self.min_value if self.stack[-1] < 0 else self.stack[-1] + self.min_value

    def getMin(self):
        return self.min_value if self.stack else -1
