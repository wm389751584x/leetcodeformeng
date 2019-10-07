class MinStack:
    # @param x, an integer
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # @return an integer
    def push(self, x):
        self.stack1.append(x)
        if len(self.stack2) == 0 or x <= self.stack2[-1]:
            self.stack2.append(x)

    # @return nothing
    def pop(self):
        top = self.stack1[-1]
        self.stack1.pop()
        if top == self.stack2[-1]:
            self.stack2.pop()

    # @return an integer
    def top(self):
        return self.stack1[-1]

    # @return an integer
    def get_min(self):
        return self.stack2[-1]


minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
print(minStack.get_min())
minStack.pop()
# minStack.pop()
print(minStack.get_min())

