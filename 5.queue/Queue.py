class ArrayQueue:
    def __init__(self, size):
        self.data = [0] * size
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, e):
        if self.isFull():
            return False
        
        # 数据搬移
        if self.tail == self.size:
            for i in range(self.head, self.tail):
                self.data[i - self.head] = self.data[i]
            self.tail -= self.head
            self.head = 0
        
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

    def show(self):
        for i in range(self.head, self.tail):
            print(self.data[i], end=" ")
        print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, e):
        node = Node(e)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
    
    def dequeue(self):
        if not self.head:
            return None

        e = self.head.data
        if not self.head.next:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return e

    def show(self):
        p = self.head
        while p:
            print("{} -> ".format(p.data), end="")
            p = p.next
        print("null")


class CircularQueue:
    def __init__(self, size):
        self.data = [0] * size
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, e):
        if self.isFull():
            return False
        
        self.data[self.tail] = e
        self.tail = (self.tail + 1) % self.size
        return True

    def dequeue(self):
        if self.isEmpty():
            return None
        e = self.data[self.head]
        self.head = (self.head + 1) % self.size
        return e

    def isEmpty(self):
        return self.head == self.tail
    
    def isFull(self):
        return (self.tail + 1) % self.size == self.head

    def show(self):
        if self.head <= self.tail:
            for i in range(self.head, self.tail):
                print(self.data[i], end=" ")
        else:
            for i in range(self.head, self.size):
                print(self.data[i], end=" ")
            for i in range(0, self.tail):
                print(self.data[i], end=" ")
        print()

if __name__ == '__main__':
#    aq = ArrayQueue(5)
#    aq.enqueue(1)
#    aq.enqueue(2)
#    aq.enqueue(3)
#    aq.enqueue(4)
#    aq.show()
#    print(aq.dequeue())
#    print(aq.dequeue())
#    aq.enqueue(5)
#    aq.enqueue(6)
#    aq.enqueue(7)
#    aq.show()
#    print(aq.isFull())

    # lq = LinkedQueue()
    # lq.enqueue(1)
    # lq.enqueue(2)
    # lq.enqueue(3)
    # lq.enqueue(4)
    # lq.show()
    # print(lq.dequeue())
    # print(lq.dequeue())
    # print(lq.dequeue())
    # lq.enqueue(5)
    # lq.enqueue(6)
    # lq.show()

    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.show()
    print(cq.isFull())
    print(cq.dequeue())
    print(cq.dequeue())
    cq.show()
    cq.enqueue(5)
    cq.enqueue(6)
    cq.show()
    print(cq.isFull())





