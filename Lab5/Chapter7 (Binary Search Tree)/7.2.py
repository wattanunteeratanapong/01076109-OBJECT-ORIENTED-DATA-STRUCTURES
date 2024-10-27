# Chapter : 7 - item : 2 - กลับด้านต้นไม้

# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ
# จากนั้นให้ สลับทุกๆ node จาก Left node เป็น Right node และจาก Right node เป็น Left node

# Test Case 1
# Enter Input : 10 2 5 11 9 3
# Before:
#       11
#  10
#                 9
#            5
#                 3
#       2
# After:
#       2
#                 3
#            5
#                 9
#  10
#       11

# Test Case 2
# Enter Input : 0 1 2
# Before:
#            2
#       1
#  0
# After:
#  0
#       1
#            2

# Test Case 3
# Enter Input : 0 -1 2
# Before:
#       2
#  0
#       -1
# After:
#       -1
#  0
#       2

# Test Case 4
# Enter Input : 0
# Before:
#  0
# After:
#  0

# Test Case 5
# Enter Input : 5 3 4 6 2 0 1
# Before:
#       6
#  5
#            4
#       3
#            2
#                      1
#                 0
# After:
#                 0
#                      1
#            2
#       3
#            4
#  5
#       6

# Test Case 6
# Enter Input : 0 2 10 1 5 3
# Before:
#            10
#                 5
#                      3
#       2
#            1
#  0
# After:
#  0
#            1
#       2
#                      3
#                 5
#            10

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data and cur.left != None:
                    cur = cur.left
                elif data >= cur.data and cur.right != None:
                    cur = cur.right
                elif data < cur.data:
                    cur.left = Node(data)
                    break
                else:
                    cur.right = Node(data)
                    break
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def reverseTree(self, node):
        if node is not None:
            node.left, node.right = node.right, node.left
            self.reverseTree(node.left)
            self.reverseTree(node.right)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

print("Before:")
T.printTree(T.root)

T.reverseTree(T.root)

print("After:")
T.printTree(T.root)
