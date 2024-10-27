# Chapter : 7 - item : 3 - พ่อจ๋าอยู่ไหน

# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ
# และให้หา พ่อ(father node) ของ node ที่กำหนด

# Test Case 1
# Enter Input : 4 3 1 2 7 6 8/1
#            8
#       7
#            6
#  4
#       3
#                 2
#            1
# 3

# Test Case 2
# Enter Input : 3 2 1 5 4 7/3
#            7
#       5
#            4
#  3
#       2
#            1
# None Because 3 is Root

# Test Case 3
# Enter Input : 1 2 3/4
#            3
#       2
#  1
# Not Found Data

class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(int(val))
        else:
            current = self.root
            while True:
                if int(val) < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(int(val))
                        break
                elif int(val) > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(int(val))
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(r, data):
    target = int(data)
    if r.data == target:
        return f"None Because {target} is Root"
    
    parent = None
    current = r
    
    while current:
        if target < current.data:
            parent = current
            current = current.left
        elif target > current.data:
            parent = current
            current = current.right
        else:
            return parent.data if parent else f"None Because {target} is Root"
    
    return "Not Found Data"

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)

printTree90(tree.root)
print(father(tree.root, data[1]))
