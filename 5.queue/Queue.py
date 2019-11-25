class ArrayQueue:
    def __init__(self, size):
        self.data = []
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, e):
        if self.isFull():
            return False
        
        if self.tail == self.size:
            count = self.tail - self.head - 1
            for i in range(0, count):
                self.data[i] = self.data[self.head]
                self.head += 1
            self.head = 0
            self.tail = count
        self.data[self.tail] = e
        self.tail += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            return None
        
        e = self.data[self.head]
        self.head += 1
        return e
    
    def isEmpty(self):
        return self.head == self.tail

    def isFull(self):
        return self.head == 0 and self.tail == self.size





