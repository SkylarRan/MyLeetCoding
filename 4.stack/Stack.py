# 基于数组实现的顺序栈， 时复空复均为O（1）
class ArrayStack:
    def __init__(self, size):
        # 栈中元素、空间大小、元素的个数
        self.data = []  
        self.size = size
        self.count = 0

    def isEmpty(self):
        return not self.count

    def isFull(self):
        return self.count == self.size

    def push(self, e):
        '''
        入栈操作
        '''
        if self.isFull():
            return False
        
        self.data.append(e)
        self.count += 1
        return True

    def pop(self):
        '''
        出栈操作
        '''
        if self.isEmpty():
            return None

        self.count -= 1
        return self.data.pop()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 基于链表实现的链式栈， 从尾部push 为O（1），pop为O（n）
# 从头部插入push，pop都为O（1）
class LinkedStack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, e):
        node = Node(e)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        # 尾部push
        # if not self.head:
        #     self.head = node
        #     self.tail = node
        # else:
        #     self.tail.next = node
        #     self.tail = node
    
    def pop(self):
        if not self.head:
            return None

        data = self.head.data
        self.head = self.head.next
        return data
        # 尾部pop
        # p = self.head
        # if not p.next:
        #     data = self.head.data
        #     self.head = None
        #     self.tail = None
        #     return data

        # while p:
        #     if p.next and p.next == self.tail:
        #         break
        #     p = p.next
        # p.next = None
        # data = self.tail.data
        # self.tail = p
        # return data

    def traverse(self):
        p = self.head
        while p:
            print("{} -> ".format(p.data), end='')
            p = p.next
        print("null")

if __name__ == '__main__':
    # stack = ArrayStack(5)
    # print(stack.push(1))
    # print(stack.push(2))
    # print(stack.push(3))
    # print(stack.push(4))
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.traverse()
    print(stack.pop())
    print(stack.pop())
    stack.traverse()
    