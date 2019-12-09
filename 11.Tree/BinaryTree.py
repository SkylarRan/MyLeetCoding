"""
array:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
  A B C D E F G H I  0  0  0  0  J
        A
     /     \ 
    B       C
   / \     / \ 
  D   E   F   G
 / \         / 
H   I       J
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class BinaryTree:
    def __init__(self, arr):
        n = len(arr)
        self.root = self.create(arr, n, 1)
    
    def create(self, arr, n, i):
        node = Node(arr[i])
        if 2*i > n or 2*i+1 > n:
            return node

        if arr[2*i] != '0':
            node.lChild = self.create(arr, n, 2*i)

        if arr[2*i+1] != '0':
            node.rChild = self.create(arr, n, 2*i+1)
    
        
            



    