class Solution:
    def trap(self, height) -> int:
        stack = []
        stack.append(height[0])
        for i in range(1, len(height)-1):
        
if __name__ == "__main__":
    solution = Solution()
    # while True:
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(solution.trap(height))