class Heap:
    def __init__(self, n):
        # 构建大顶堆
        self.n = n # 堆中存储节点的最大个数
        self.a = [0] * (n+1)
        self.count = 0 #堆中已经存放的节点个数
        self.swapCount = 0

    def create(self, arr):
        '''
        建堆：从第一个非叶子节点开始进行从上往下堆化
        '''
        self.count = len(arr)
        for i in range(len(arr)):
            self.a[i+1] = arr[i]

        # 第一个非叶子节点为中点
        for j in range(self.count//2, 0, -1):
            self.heapify(j)

    def insert(self, val):
        # 堆满了
        if self.n == self.count:
            return  
        
        # 从下往上堆化
        self.count += 1
        i = self.count
        self.a[i] = val

        while (i//2) > 0 and self.a[i//2] < self.a[i]:
            tmp = self.a[i]
            self.a[i] = self.a[i//2]
            self.a[i//2]  = tmp
            i = i//2

    def removeMax(self):
        ''' 删除堆顶元素 '''
        
        if self.count == 0:
            return
        
        # if self.count == 1:
            # self.a[1] 
        self.a[1] = self.a[self.count]
        self.count -= 1
        self.heapify(1)

    def heapify(self, i):
        '''（大顶堆）自上而下堆化'''
        m = i
        while True:
            if 2*i <= self.count and self.a[m] < self.a[2 * i]:
                m = 2 * i
            
            if 2*i+1 <= self.count and self.a[m] < self.a[2*i+1]:
                m = 2*i + 1
            
            if m == i:
                break
            else:
                self.swapCount += 1
                tmp = self.a[i]
                self.a[i] = self.a[m]
                self.a[m] = tmp
                i = m

    def sort(self, arr):
        self.create(arr)
        count = self.count
        for i in range(count, 1, -1):
            tmp = self.a[i]
            self.a[i] = self.a[1]
            self.a[1] = tmp
            self.count -= 1
            self.swapCount += 1
            self.heapify(1)
        self.count = count

    def show(self):
        for i in range(1, self.count+1):
            print(self.a[i], end=' ')
        print()


if __name__ == '__main__':
    h = Heap(20)
    arr = [7,5,19,8,4,1,20,13,16,31]
    # h.create(arr)
    # h.show()
    h.sort(arr)
    print(h.swapCount)
    h.show()

    # h = Heap(20)
    # h.insert(33)
    # h.insert(27)
    # h.insert(21)
    # h.insert(16)
    # h.insert(13)
    # h.insert(15)
    # h.insert(9)
    # h.insert(5)
    # h.insert(6)
    # h.insert(7)
    # h.insert(8)
    # h.insert(1)
    # h.insert(2)
    # h.show()

    # h.insert(22)
    # h.show()

    # h.removeMax()
    # h.show()

    # h.removeMax()
    # h.show()