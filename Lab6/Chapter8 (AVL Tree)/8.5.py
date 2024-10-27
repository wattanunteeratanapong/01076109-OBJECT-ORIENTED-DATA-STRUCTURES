# Chapter : 8 - item : 5 - Cut The Tree

# พี่โบ๊ทเป็นชาวสวนกำลังจะตัดกิ่งไม้ของ Binary Search Tree ออกมาเป็น ต้นไม้ย่อย ๆ 2 ต้น ก็คือ ต้นไม้ที่ถูกตัดออกมาและต้นไม้ที่เหลือจากการถูกตัด แต่ด้วยความเป็น Perfectionism ของพี่โบ๊ทเอง เขาคันไม้คันมือตัดแต่งต้นไม้ย่อย ๆ ให้เป็น AVL Tree เพื่อให้ต้นไม้ดูสวยงามมากขึ้น
# หมายเหตุ: เนื่องจาก อาทิตย์ที่แล้ว พี่ไม่ได้ออก Binary Search Tree แล้วกลัวน้อง ๆ จะเซ็งที่พี่ไม่ออกโจทย์ พี่เลยยำรวม 2 หัวข้อเป็นข้อเดียวซะเลย :>
# แต่ทั้งนี้เพื่อลดความลำบากของน้อง ๆ พี่เลยใจดีให้ Prototype Code คร่าวๆ ให้ หรือ จะเขียนใหม่ก็ได้ไม่บังคับ
# อธิบายข้อมูลนำเข้า
# Enter the val of tree and node to cut (e.g. '1 2 3 4 / 2'): 8 3 10 1 6 14 4 7/3
# Enter the val of tree and node to cut: 8 3 10 1 6 14 4 7/3
# Before cut:
#          14
#      10
#  8
#              7
#          6
#              4
#      3
#          1
# Cutted Tree:
#         7
#     6
#         4
# 3
#     1
# Left Tree:
#     14
# 10
#     8
# Before Cut แสดงต้นไม้ก่อนที่จะตัดในรูปแบบ Binary Search Tree
# Cutted Tree แสดงต้นไม้ที่ตัดออกมาในรูปแบบ AVL Tree
# Left Tree แสดงต้นไม้ที่เหลือออกมาในรูปแบบ AVL Tree
# จากข้อมูลนำเข้า /3 คือ ตัดต้นไม้ตรง Node ที่มีค่าเท่ากับ 3 ออกมาจะได้
# ต้นไม้ที่ตัดออกมา (Cutted Tree)
#         7
#     6
#         4
# 3
#     1
# ต้นไม้ที่เหลือ (Left Tree)
#         14
#     10
# 8
# แต่ต้นไม้ยังไม่ Balanced จึงทำการแปลงเป็น AVL Tree เป็น
#     14
# 10
#     8
# รับประกันว่า Node ที่ Input เข้ามาจะมีในต้นไม้หลักแน่นอน

# Test Case 1
# Enter the val of tree and node to cut: 8 3 10 1 6 14 4 7/3
# Before cut:
#         14
#     10
# 8
#             7
#         6
#             4
#     3
#         1
# Cutted Tree:
#         7
#     6
#         4
# 3
#     1
# Left Tree:
#     14
# 10
#     8

# Test Case 2
# Enter the val of tree and node to cut: 10 4 20 1 5/4
# Before cut:
#     20
# 10
#         5
#     4
#         1
# Cutted Tree:
#     5
# 4
#     1
# Left Tree:
#     20
# 10

# Test Case 3
# Enter the val of tree and node to cut: 1 2 3 4 5 6 7 8 0 -1 -2/4
# Before cut:
#                             8
#                         7
#                     6
#                 5
#             4
#         3
#     2
# 1
#     0
#         -1
#             -2
# Cutted Tree:
#         8
#     7
#         6
# 5
#     4
# Left Tree:
#         3
#     2
# 1
#         0
#     -1
#         -2

# Test Case 4
# Enter the val of tree and node to cut: 4999 2353 8574 9324 234 4395 415 1358 6712 8558/234
# Before cut:
#         9324
#     8574
#             8558
#         6712
# 4999
#         4395
#     2353
#                 1358
#             415
#         234
# Cutted Tree:
#     1358
# 415
#     234
# Left Tree:
#         9324
#     8574
#         8558
# 6712
#         4999
#     4395
#         2353

class BST:
    class BSTNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, root=None) -> None:
        self.root = root

    def get_successor(self, curr):
        curr = curr.right
        while curr.left is not None:
            curr = curr.left
        return curr

    def search_subtree(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search_subtree(root.left, key)
        return self.search_subtree(root.right, key)

    def insert(self, root, key):
        if root is None:
            return self.BSTNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def delete_subtree(self, root, key):
        if root is None:
            return None

        if key < root.val:
            root.left = self.delete_subtree(root.left, key)
        elif key > root.val:
            root.right = self.delete_subtree(root.right, key)
        else:
            return None  

        return root

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.val))
            self.printTree90(root.left, indent + 1)


class AVLTree:
    class AVLNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right
            self.height = 1

    def __init__(self, root=None) -> None:
        self.root = root

    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        if root is None:
            return self.AVLNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def bst_to_avl(self, bst_root):
        sorted_values = self.inorder_traversal(bst_root)
        for val in sorted_values:
            self.root = self.insert(self.root, val)

    def inorder_traversal(self, root):
        if root is None:
            return []
        return (
            self.inorder_traversal(root.left)
            + [root.val]
            + self.inorder_traversal(root.right)
        )

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.val))
            self.printTree90(root.left, indent + 1)


inp1, inp2 = input("Enter the val of tree and node to cut: ").split("/")
bst = BST()
for i in inp1.split():
    bst.root = bst.insert(bst.root, int(i))

print("Before cut:")
bst.printTree90(bst.root)

avl1, avl2 = AVLTree(), AVLTree()

print("Cutted Tree:")
subtree_root = bst.search_subtree(bst.root, int(inp2))
avl1.bst_to_avl(subtree_root)
avl1.printTree90(avl1.root)

print("Left Tree:")
bst.root = bst.delete_subtree(bst.root, int(inp2))
avl2.bst_to_avl(bst.root)
avl2.printTree90(avl2.root)
