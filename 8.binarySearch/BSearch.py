class BSearch:
    def __init__(self, nums, e):
        self.nums = nums
        self.e = e

    def base_iteration(self):
        low, high = 0, len(self.nums)-1
        while low <= high:
            mid = low + ((high - low)>>1)
            if self.nums[mid] == self.e:
                return mid
            elif self.nums[mid] < self.e:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def base_recursion(self):
        return self.recursive(0, len(self.nums)-1)

    def recursive(self, low, high):
        if low > high:
            return -1
        
        mid = low + ((high - low)>>1)
        if self.nums[mid] == self.e:
            return mid
        elif self.nums[mid] < self.e:
            return self.recursive(mid+1, high)
        else:
            return self.recursive(low, mid - 1)


if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    e = 5
    bs = BSearch(nums, e)
    print(bs.base_iteration())
    print(bs.base_recursion())