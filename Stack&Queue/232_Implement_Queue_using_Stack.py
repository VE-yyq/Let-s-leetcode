class MyQueue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self,x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop()
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1]
        else:
            return self.s2[-1]
    def empty(self):
        if not self.s2 and not self.s1:
            return True
        else:
            return False

