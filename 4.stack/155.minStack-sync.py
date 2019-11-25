class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.helper) == 0 or x < self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.helper.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-1)
    minStack.push(2)
    minStack.push(-3)
    print('top:{}'.format(minStack.top()))
    print('min:{}'.format(minStack.getMin()))
    minStack.pop()
    print('top:{}'.format(minStack.top()))
    print('min:{}'.format(minStack.getMin()))
          