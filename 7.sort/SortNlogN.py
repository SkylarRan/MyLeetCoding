class Sort:
    def __init__(self, nums):
        self.nums = nums

    def MergeSort(self):
        self.merge_sort_c(0, len(self.nums) - 1)

    def merge_sort_c(self, l, r):
        if l >= r:
            return
        mid = (l + r) // 2
        self.merge_sort_c(l, mid)
        self.merge_sort_c(mid+1, r)
        # self.merge(l, mid, r)
        self.merge1(l, mid, r)

    def merge(self, l, mid, r):
        i, j = l, mid+1
        helper = []
        while i<=mid and j<=r:
            if self.nums[i] <= self.nums[j]:
                helper.append(self.nums[i])
                i += 1
            else:
                helper.append(self.nums[j])
                j += 1

        start, end = i, mid
        if j<=r :
            start, end = j, r
        
        while start <= end:
            helper.append(self.nums[start])
            start += 1
        
        for i in range(len(helper)):
            self.nums[l+i] = helper[i]
        
        self.show()

    # 利用哨兵简化合并
    def merge1(self, l, mid, r):
        i, j = l, mid+1
        helper = []
        while i<=mid or j<=r:
            if j > r or (self.nums[i] <= self.nums[j] and i<=mid):
                helper.append(self.nums[i])
                i += 1
            else:
                helper.append(self.nums[j])
                j += 1

        for i in range(len(helper)):
            self.nums[l+i] = helper[i]
        
        self.show()


    def QuickSort(self):
        self.quick_sort_c(0, len(self.nums) - 1)

    def quick_sort_c(self, l, r):
        if l>=r:
            return
        
        q = self.partition(l, r)
        self.show()
        self.quick_sort_c(l, q-1)
        self.quick_sort_c(q+1, r)
    
    def partition(self, l, r):
        qivot = self.nums[r]
        j = l
        for i in range(l, r):
            if self.nums[i] < qivot:
                tmp = self.nums[i]
                self.nums[i] = self.nums[j]
                self.nums[j] = tmp
                j += 1

        self.nums[r] = self.nums[j]
        self.nums[j] = qivot
        return j

    def show(self):
        for i in range(len(self.nums)):
            print(self.nums[i], end=" ")
        print()


if __name__ == '__main__':
    nums = [16,1,35,4,33,22]
    s = Sort(nums)
    s.MergeSort()
    # s.QuickSort()