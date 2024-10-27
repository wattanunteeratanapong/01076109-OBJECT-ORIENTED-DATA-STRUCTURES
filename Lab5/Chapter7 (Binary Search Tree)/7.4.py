# Chapter : 7 - item : 4 - สนุกไปกับ Binary Search Tree

# ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ

# Test Case 1
# Enter Input : 10 4 20 1 5
# Preorder : 10 4 1 5 20 
# Inorder : 1 4 5 10 20 
# Postorder : 1 5 4 20 10 
# Breadth : 10 4 20 1 5 

# Test Case 2
# Enter Input : 0 -50 50 25 -25 13 -13 28 -38 75 -75 62 -62 100 -100
# Preorder : 0 -50 -75 -100 -62 -25 -38 -13 50 25 13 28 75 62 100 
# Inorder : -100 -75 -62 -50 -38 -25 -13 0 13 25 28 50 62 75 100 
# Postorder : -100 -62 -75 -38 -13 -25 -50 13 28 25 62 100 75 50 0 
# Breadth : 0 -50 50 -75 -25 25 75 -100 -62 -38 -13 13 28 62 100 

class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 

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

    def preorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.data)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        return result

    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)
        return result

    def postorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.data)
        return result

    def bfs(self):
        queue = []
        result = []
        if self.root:
            queue.append(self.root)
        while queue:
            current = queue.pop(0)
            result.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

tree = BinarySearchTree()
data = input("Enter Input : ").split()
for e in data:
    tree.create(e)

print("Preorder : " + ' '.join(map(str, tree.preorder(tree.root))))
print("Inorder : " + ' '.join(map(str, tree.inorder(tree.root))))
print("Postorder : " + ' '.join(map(str, tree.postorder(tree.root))))
print("Breadth : " + ' '.join(map(str, tree.bfs())))
