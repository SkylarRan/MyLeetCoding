class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list()
        stack = []
        mappings = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char in mappings:
                top_element = stack.pop() if stack else '#'
                if mappings[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


if __name__ == "__main__":
    solution = Solution()
    while True:
        s = input()
        print(solution.isValid(s))