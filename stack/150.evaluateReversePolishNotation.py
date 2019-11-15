class Solution:
    def evalRPN(self, tokens) -> int:
        operator = ["+", "-", "*", "/"]
        stack = []
        for t in tokens:
            if not t in operator:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                i = operator.index(t)
                if i == 0:
                    c = a + b
                elif i == 1:
                    c = a - b
                elif i == 2:
                    c = a * b
                else: 
                    c = a // b
                
                stack.append(c)
        return stack[0]


if __name__ == "__main__":
    solution = Solution()
    # while True:
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(solution.evalRPN(tokens))