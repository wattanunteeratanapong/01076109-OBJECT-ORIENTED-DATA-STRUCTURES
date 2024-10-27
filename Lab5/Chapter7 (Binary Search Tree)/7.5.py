# Chapter : 7 - item : 5 - ส่วนไหน

# นำ code จากข้อ 1 มาเปลี่ยนเป็น

# T = BST()
# inp = [int(i) for i in input('Enter Input : ').split()]
# for i in range(1, len(inp)):
#     root = T.insert(inp[i])
# T.printTree(root)
# T.checkpos(inp[0])

# เพื่อหาว่าค่าแรกที่ใส่เข้าไปอยู่ที่ตำแหน่งใดใน BST

# ##code output
# print("Not exist")
# print("Root")
# print("Inner")
# print("Leaf")

# Test Case 1
# Enter Input : 30 10 4 20 1 5
#       20
#  10
#            5
#       4
#            1
# Not exist

# Test Case 2
# Enter Input : 4 4 10 3 6 13 9
#            13
#       10
#                 9
#            6
#  4
#       3
# Root

# Test Case 3
# Enter Input : 10 7 10 3 6 13 9
#            13
#       10
#            9
#  7
#            6
#       3
# Inner

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
            current = self.root
            while True:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break
        return self.root
    
    def printTree(self, node, level=0):
        if node:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self, data):
        current = self.root
        parent = None

        while current:
            if data < current.data:
                parent = current
                current = current.left
            elif data > current.data:
                parent = current
                current = current.right
            else:
                if current == self.root:
                    print("Root")
                elif current.left or current.right:
                    print("Inner")
                else:
                    print("Leaf")
                return

        print("Not exist")

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])
