class Solution:
    def simplifyPath(self, path: str) -> str:
        data = path.split('/')
        stack = []
        for d in data:
            if d == '' or d == '.':
                pass
            elif d == '..':
                stack.pop() if stack else '#'
            else:
                stack.append(d)

        # str = '-'
        # seq = ["a","b","c"]
        # str.join(seq) = "a-b-c"
        return "/" + "/".join(stack)



if __name__ == "__main__":
    solution = Solution()
    while True:
        str = input()
        print(solution.simplifyPath(str))