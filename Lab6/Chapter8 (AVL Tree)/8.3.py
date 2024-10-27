# Chapter : 8 - item : 3 - AVL: Tree

# ให้นักศึกษาสร้าง AVL Tree แล้วแสดงผล Tree ในแต่ละรอบหลังจาก insert และตรวจสอบว่า Balance หรือเปล่าถ้าไม่ Balance ปรับให้เรียบร้อยและแสดงรอบแบบการปรับ Tree ว่าเป็นการ Rotation แบบไหน
# ตัวอย่างการทำงาน
#  *** AVL Tree Insert Element ***
# Enter Input : 1 2 3 4
# insert : 1
#  1
# ====================
# insert : 2
#       2
#  1
# ====================
# insert : 3
# Left Left Rotation
#       3
#  2
#       1
# ====================
# insert : 4
#            4
#       3
#  2
#       1
# ====================

# Test Case 1
#  *** AVL Tree Insert Element ***
# Enter Input : 1 2 3 4
# insert : 1
#  1
# ====================
# insert : 2
#       2
#  1
# ====================
# insert : 3
# Left Left Rotation
#       3
#  2
#       1
# ====================
# insert : 4
#            4
#       3
#  2
#       1
# ====================

# Test Case 2
#  *** AVL Tree Insert Element ***
# Enter Input : 28 18 38 10 20 30 40
# insert : 28
#  28
# ====================
# insert : 18
#  28
#       18
# ====================
# insert : 38
#       38
#  28
#       18
# ====================
# insert : 10
#       38
#  28
#       18
#            10
# ====================
# insert : 20
#       38
#  28
#            20
#       18
#            10
# ====================
# insert : 30
#       38
#            30
#  28
#            20
#       18
#            10
# ====================
# insert : 40
#            40
#       38
#            30
#  28
#            20
#       18
#            10
# ====================

class TreeNode:
    def __init__(self, val):
        self.val = int(val)
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)

class AVL_Tree:
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        print("Right Right Rotation")
        return y

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        print("Left Left Rotation")
        return y

    def leftRightRotate(self, z):
        z.left = self.leftRotate(z.left)
        print("Left Right Rotation")
        return self.rightRotate(z)

    def rightLeftRotate(self, z):
        z.right = self.rightRotate(z.right)
        print("Right Left Rotation")
        return self.leftRotate(z)

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif int(key) < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and int(key) < root.left.val:
            return self.rightRotate(root)

        if balance < -1 and int(key) > root.right.val:
            return self.leftRotate(root)

        if balance > 1 and int(key) > root.left.val:
            return self.leftRightRotate(root)

        if balance < -1 and int(key) < root.right.val:
            return self.rightLeftRotate(root)

        return root

def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

print(" *** AVL Tree Insert Element ***")
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :", e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("====================")
