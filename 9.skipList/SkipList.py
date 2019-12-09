Max_LEVEL = 16

class Node:
    def __init__(self, data, level):
        self.data = data
        self.max_level = level
        self.forwards = []
    

class skipList:
    def __init__(self):
        self.head = Node(-1, Max_LEVEL) # 带头链表
        self.levelCount = 1

    def insert(self, value):
        level = self.randomLevel()
        newNode = Node(value, level)
        
        # 找到新数据要插在对应索引层的哪个结点之后，update用于存放这些结点
        # update初始化为头结点
        update = []
        for i in range(level):
            update.append(self.head) 

        p = self.head

        for i in range(level-1, -1, -1):
            while p.forwards[i] != None and p.forwards[i].data < value:
                p = p.forwards[i]
            update[i] = p

        # 将新结点插入对应索引层中
        for i in range(level):
            newNode.forwards.append(update[i].forwards[i])
            update[i].forwards[i] = newNode

        if self.levelCount < level:
            self.levelCount = level
        
    def find(self, value):
        p = self.head
        for i in range(self.levelCount-1, -1 , -1):
            while p.forwards[i] != None and p.forwards[i].data < value:
                p = p.forwards[i]




        




    def randomLevel(self):
        level = 1
        return level

if __name__ == '__main__':
    print(Max_LEVEL)