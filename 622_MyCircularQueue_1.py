class MyCircularQueue:

    def __init__(self, k: int):
        self.circurque = [-1] * k
        self.head = 0
        self.tail = 0
        self.k = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size >= self.k:
            return False
        self.circurque[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        
        if self.size == -1:
            return False
        self.circurque[self.head] = -1
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.circurque[self.head]
        

    def Rear(self) -> int:

        if self.tail == 0:
            return self.circurque[self.k - 1]
        return self.circurque[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
        
res = []
obj = MyCircularQueue(3)
res.append(obj.enQueue(6))
res.append(obj.Rear())
res.append(obj.Rear())
res.append(obj.deQueue())
res.append(obj.enQueue(5))
res.append(obj.Rear())
res.append(obj.deQueue())
res.append(obj.Front())
res.append(obj.deQueue())
res.append(obj.deQueue())
res.append(obj.deQueue())




print(res)





# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()