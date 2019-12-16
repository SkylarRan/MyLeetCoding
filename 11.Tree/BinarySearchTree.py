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
        while p and p.data != val:
            pp = p
            if p.data > val:
                p = p.left
            else:
                p = p.right
            
        if p == None:
            return False # 没找到要删除的节点

        #要删除的节点有两个子节点
        if p.left and p.right:
            # 1. 找到该节点的右子树的最小节点minP  
            minP = p.right
            minPP = p   # minPP为最小节点的父节点
            while minP.left:
                minPP = minP
                minP = minP.left
            # 2. 用该节点的值为minP的值
            p.data = minP.data
            # 3.删除minP(相当于删除叶子节点或只有一个右子节点的节点)
            p = minP
            pp = minPP

        # 要删除的节点是叶子节点或者只有一个子节点
        if p.left:
            child = p.left
        elif p.right:
            child = p.right
        else:
            child = None
            
        # 考虑要删除根节点
        if p == self.root:
            self.root = child
            return True
        if p == pp.left:
            pp.left = child
        else:
            pp.right = child

        return True

    def getMaxAndMin(self):
        p = self.root
        while p and p.left:
            p = p.left
        minV = p.data

        p = self.root
        while p and p.right:
            p = p.right
        maxV = p.data
        return minV, maxV
    
    def getPreAndNext(self, val):
        # 前驱（父节点）和后继节点（左右节点）
        p = self.root
        while p and p.data != val:
            pp = p
            if p.data > val:
                p = p.left
            else:
                p = p.right
            
        if p == None:
            return None
        
        if p == self.root:
            pre = None
        else:
            pre = pp.data
       
        nxt = [p.left.data if p.left else None, p.right.data if p.right else None]
        return pre, nxt

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
    b.insert(28)
    b.insert(30)
    b.insert(29)
    b.insert(31)
    b.inOrder(b.root)
    print()
    print(b.root.data)


    b.remove(50)
    b.inOrder(b.root)  
    print()  
    print(b.root.data)
    print(b.getMaxAndMin())
    print(b.getPreAndNext(25))





