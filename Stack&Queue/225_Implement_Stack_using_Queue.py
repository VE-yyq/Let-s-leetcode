import collections


class MyStack:
    def __init__(self):
        # 使用两个双端队列来模拟,q1用于存储，q2辅助入栈操作
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x):
        self.queue2.append(x)  # 新元素入队q2
        while self.queue1:  # q1元素全部入队q2
            self.queue2.append(self.queue1.popleft())
        # 队列互换，前端栈顶，后端栈底
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        # 由于每次入栈都确保q1前端为栈顶元素，出栈移除并返回即可
        return self.queue1.popleft()

    def top(self):
        # 获得栈顶元素不用移除
        return self.queue1[0]

    def empty(self):
        if self.queue1:
            return False
        else:
            return True
