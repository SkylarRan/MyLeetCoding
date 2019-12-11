'''
Tree:
              20
        |            |
      15             28
   |     |       |        | 
  10     18      24      59
|    |  |   |   |   |   |   |  
3   12  0   0   0   0   40  0

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, arr):
        self.root = self._create(arr, len(arr), 1)

    def _create(self, arr, n, i):
        node = Node(arr[i])

        if 2*i < n and arr[2*i] != 0:
            node.left = self._create(arr, n, 2*i)
        
        if 2*i+1 < n and arr[2*i+1] != 0:
            node.right = self._create(arr, n, 2*i+1)
        
        return node

    def inOrder(self, root):
        if root == None:
            return 
        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)

    def find(self, val):
        c = self.root
        while c:
            if c.data > val:
                c = c.left
            elif c.data < val:
                c = c.right
            else:
                return c
        return None

    def insert(self, val):
        newNode = Node(val)
        if self.root == None:
            self.root = newNode
            return

        c = self.root
        while c:
            if c.data > val:
                if c.left == None:
                    c.left = newNode
                    return
                else:
                    c = c.left
            else:
                if c.right == None:
                    c.right = newNode
                    return
                else:
                    c = c.right

    def remove(self, val):
        # p指要删除的节点， pp指该节点的父节点
        p = self. root
        while p:
            if p.data > val:
                pp = p
                p = p.left
            elif p.data < val:
                pp = p
                p = p.right
            else:
                break
            
        if p == None:
            return False # 没找到要删除的节点
        
        # if p == self.root:

        # 要删除的节点是叶子节点或者只要一个节点
        if p.left == None or p.right == None:            
            
            if pp.left == p:
                pp.left = p.left if p.right == None else p.right
            else:
                pp.right = p.left if p.right == None else p.right
            
            return True
            
        #要删除的节点有两个子节点
        # 1. 找到该节点的右子树的最小节点 2. 用最小节点替代该节点 3. 修改父节点的子节点
        # m为最小节点， mp为最小节点的父节点
        m = p.right
        while m.left:
            mp = m
            m = m.left
        if m == p.right:
        else:
        


if __name__ == '__main__':
    # arr = [0, 20, 15, 28, 10, 18, 24, 59, 3, 12, 0, 0, 0, 0, 40]
    # bst = BinarySearchTree(arr)
    # bst.inOrder(bst.root)
    # node = bst.find(15)
    # bst.insert(25)
    # print()
    # bst.inOrder(bst.root)
    
    b = BinarySearchTree([0,50])
    b.insert(25)
    b.insert(4)
    b.insert(16)
    b.insert(80)
    b.insert(67)
    b.insert(95)
    b.insert(72)
    b.inOrder(b.root)

    b.remove(50)
    b.inOrder(b.root)    






