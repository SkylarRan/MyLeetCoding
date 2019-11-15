class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self) -> None:
        if self.stack:
            if self.helper and self.stack[-1] == self.helper[-1]:
                self.helper.pop()
            self.stack.pop()   

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.push(-3)
    minStack.push(6)
    minStack.push(-3)
    
    for i in range(len(minStack.stack)):
        print('top:{}'.format(minStack.top()))
        print('min:{}'.format(minStack.getMin()))
        minStack.pop()
          