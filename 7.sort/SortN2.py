class Sort:
    def __init__(self, nums):
        self.nums = nums

    def BubbleSort(self):
        n = len(self.nums)
        for i in range(n - 1):
            for j in range(n-i-1):
                if self.nums[j] > self.nums[j+1]:
                    tmp = self.nums[j]
                    self.nums[j] = self.nums[j+1]
                    self.nums[j+1] = tmp
            self.show()

    def BubbleSort1(self):
        n = len(self.nums)
        for i in range(n - 1):
            swap = False
            for j in range(n-i-1):
                if self.nums[j] > self.nums[j+1]:
                    swap = True
                    tmp = self.nums[j]
                    self.nums[j] = self.nums[j+1]
                    self.nums[j+1] = tmp
            self.show()
            # 此轮无数据交换则停止
            if not swap: 
                break

    def InsertSort(self):
        for i in range(1, len(self.nums)):
            value = self.nums[i]
            for j in range(i-1, -1, -1):
                if self.nums[j] > value:
                    self.nums[j + 1] = self.nums[j]
                else:
                    break
            # 此处判断j == 0是因为python的for循环中当j为0时，不会再执行j--， 而Java和C++中会在执行到j = -1
            if j == 0:
                self.nums[j] = value
            else:
                self.nums[j+1] = value
            self.show()

    def SelectSort(self):
        for i in range(len(self.nums)-1):
            m = i
            for j in range(i+1, len(self.nums)):
                if self.nums[m] > self.nums[j]:
                    m = j
            if i == m:
                continue
            tmp = self.nums[i]
            self.nums[i] = self.nums[m]
            self.nums[m] = tmp
            self.show()

    def show(self):
        for i in range(len(self.nums)):
            print(self.nums[i], end=" ")
        print()


if __name__ == '__main__':
    # nums = [6,5,4,3,2,1]
    # s = Sort(nums)
    # s.BubbleSort()

    nums = [2,5,1,4,6,3]
    s = Sort(nums)
    # s.BubbleSort1()
    s.InsertSort()
    # s.SelectSort()