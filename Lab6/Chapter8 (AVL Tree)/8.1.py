# Chapter : 8 - item : 1 - AVL : Traversal

# จงเขียนโปรแกรมเพื่อรับข้อมูล แล้วสร้าง AVL tree และแสดงการแวะผ่านโหนดต่าง ๆ แบบ post-order
# โดยแก้ไข method add คือการเพิ่มข้อมูลเข้าใน AVLTree และ method postOrder คือ บริการแวะผ่านโหนดทุกโหนดแบบหลังลำดับ จากส่วนของโปรแกรมต่อไปนี้

# Test Case 1
# Enter Input : AD 10,AD 5,AD 15,PR,PO,AD 20,AD 8,PR,PO
#       15
#  10
#       5
# AVLTree post-order : 5 15 10 
#            20
#       15
#  10
#            8
#       5
# AVLTree post-order : 8 5 20 15 10 

# Test Case 2
# Enter Input : AD 1,AD -2,AD 0,AD 8,AD 8,AD 7,AD -9,AD -10,AD 3,AD 11,PR,PO
#                 11
#            8
#       8
#            7
#                 3
#  1
#            0
#       -2
#            -9
#                 -10
# AVLTree post-order : -10 -9 0 -2 3 7 11 8 8 1 

# Test Case 3
# Enter Input : AD 1,AD 2,AD 3,PR,AD 4,AD 5,PR,PO
#       3
#  2
#       1
#            5
#       4
#            3
#  2
#       1
# AVLTree post-order : 1 3 5 4 2 

# Test Case 4
# Enter Input : PR,PO
# AVLTree post-order : 

# Test Case 5
# Enter Input : AD 5,AD 4,AD 3,PR,AD 2,AD 1,PR,PO
#       5
#  4
#       3
#       5
#  4
#            3
#       2
#            1
# AVLTree post-order : 1 3 2 5 4 

# Test Case 6
# Enter Input : AD 9,AD -2,AD 100,AD 8,AD 8,PR,PO,AD 7,AD -90,AD -10,AD 3,AD 11,PR,PO
#       100
#  9
#            8
#       8
#            -2
# AVLTree post-order : -2 8 8 100 9 
#            100
#                 11
#       9
#            8
#  8
#            7
#                 3
#       -2
#                 -10
#            -90
# AVLTree post-order : -10 -90 3 7 -2 8 11 100 9 8 

class AVLTree:

    class AVLNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a, b)
            return self.height

        def getHeight(self, node):
            return -1 if node is None else node.height

        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self, root=None):
        self.root = None if root is None else root

    def add(self, data):
        self.root = AVLTree._add(self.root, data)

    def _add(root, data):
        if not root:
            return AVLTree.AVLNode(data)
        if data < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)

        root.setHeight()

        balance = root.balanceValue()

        if balance < -1:
            if data < root.left.data:  # Left-left case
                return AVLTree.rotateRightChild(root)
            else:  # Left-right case
                root.left = AVLTree.rotateLeftChild(root.left)
                return AVLTree.rotateRightChild(root)

        if balance > 1:
            if data > root.right.data: 
                return AVLTree.rotateLeftChild(root)
            else:
                root.right = AVLTree.rotateRightChild(root.right)
                return AVLTree.rotateLeftChild(root)

        return root

    def rotateLeftChild(root):
        newRoot = root.right
        if newRoot is None:
            return root
        
        root.right = newRoot.left
        newRoot.left = root

        root.setHeight()
        newRoot.setHeight()

        return newRoot

    def rotateRightChild(root):
        newRoot = root.left
        if newRoot is None:
            return root
        root.left = newRoot.right
        newRoot.right = root

        root.setHeight()
        newRoot.setHeight()

        return newRoot

    def postOrder(self):
        print("AVLTree post-order : " , end='')
        AVLTree._postOrder(self.root)

    def _postOrder(root):
        if root is None:
            return
        AVLTree._postOrder(root.left)
        AVLTree._postOrder(root.right)
        print(root.data, end=' ')

    def printTree(self):
        AVLTree._printTree(self.root)

    def _printTree(node, level=0):
        if node is not None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)


avl1 = AVLTree()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AD":
        avl1.add(int(i[3:])) 
    elif i[:2] == "PR":
        avl1.printTree()
        print()
    elif i[:2] == "PO":
        avl1.postOrder()
        print()
