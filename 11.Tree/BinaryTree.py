from queue import Queue

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
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, arr):
        n = len(arr)
        self.root = self.create(arr, n, 1)
    
    def create(self, arr, n, i):
        node = Node(arr[i])
        if 2*i < n and arr[2*i] != '0':
            node.left = self.create(arr, n, 2*i)

        if 2*i+1 < n and arr[2*i+1] != '0':
            node.right = self.create(arr, n, 2*i+1)

        return node

    def preOrder(self, root):
        if root == None:
            return
        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)

    def postOrder(self, root):
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=" ")

    def floorOrder(self, root):
        """
            按层遍历，需要借助一个队列来实现
        """
        if root == None:
            return
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            print(node.data, end=" ")
            if node.left != None:
                q.put(node.left)

            if node.right != None:
                q.put(node.right)



if __name__ == '__main__':
    arr = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '0', '0', '0', '0', 'J']
    tree = BinaryTree(arr)
    tree.preOrder(tree.root)
    print()
    tree.inOrder(tree.root)
    print()
    tree.postOrder(tree.root)
    print()
    tree.floorOrder(tree.root)
        
            



    