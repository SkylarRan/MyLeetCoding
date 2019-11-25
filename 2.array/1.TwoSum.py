class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            dict[target - nums[i]] = nums[i]

        for i in range(len(nums)):
            val = dict.get(nums[i])
            if val is not None:
                if val == nums[i] and nums.count(val) > 1:
                    return [i , nums.index(dict[nums[i]], i+1)]
                else:
                    return [i, nums.index(dict[nums[i]])]


if __name__ == "__main__":
    solution = Solution()
    # while True:
    nums = [2,5,5,11]
    target = 10
    print(solution.twoSum(nums, target))