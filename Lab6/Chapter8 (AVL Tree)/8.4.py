# Chapter : 8 - item : 4 - Burn The Tree!!!

# พี่ว่าการสร้าง Tree มันยากเกินไปและใช้เวลานานมาก กว่าต้นไม้จะโต เพราะฉะนั้นเราจะทำอะไรให้มันเร็วกว่าการปลูกต้นไม้ดีกว่า นั่นคือการ เผามันทิ้งไปเลย ยังไงล่ะ

# โดยที่เดี๋ยวพี่จะจุดไฟใส่ กิ่ง หรือ ใบไม้สักใบนึง แล้วดูว่าพอเวลาผ่านไปทุกๆนาที จะมีส่วนไหนของต้นไม้บ้างที่ไหม้เกรียมไปแล้วบ้าง 

# หลักการทำงานคร่าวๆ 
# 1.สร้าง AVL Tree ด้วยความตั้งใจ (ตัวแรกไม่จำเป็นต้องเป็น Root เสมอไป)
# 2.จุดไฟที่ node นั้น -> ถือว่า node นั้นไหม้ไปแล้ว
# 3.ทุกๆนาที จะมี กิ่ง หรือ ใบ รอบๆข้างที่เชื่อมต่อกับ node นั้นไหม้ทั้งหมด
# 4.โดยให้วนดูจาก left child node ของ node นั้นก่อนเสมอ
# 5.ตามด้วย right child node 
# 6.ปิดท้ายด้วย parent node ของ node นั้น 
# 7.ถ้าไม่มี node ที่อยู่ติดกับ node ที่ไหม้ไปแล้ว ก็ปล่อยมันไป
# 8.บอกพี่หน่อยว่า แต่ละนาที มี node ไหนที่ไหม้ไปบ้าง
# 9.เช่น Testcase #1 : Node ที่จะเผาคือ Node(14)

#               14
#       12               21
#   10     13     15       23
#                        22  24

# Minute 0 : 14 				(เผาอยู่)
# Minute 1 : 12 21 			(ไฟลามไปทาง left child node แล้วค่อยไป right child node)
# Minute 2 : 10 13 15 23 	(ไฟลามเหมือนเดิม วนไป)
# Minute 3 : 22 24 			(Node(10), Node(13) ไม่มีตัวต่อแล้ว ก็ไม่ต้องสนอะไร ไฟลามไป child ของ node ที่เหลือแทน)

# Test Case 1
# Enter node and burn node : 12 14 21 22 13 15 10 23 24/14
#               14               
#       12               21       
#   10       13       15       23   
#                         22   24 
# 14
# 12 21 
# 10 13 15 23 
# 22 24 

# Test Case 2
# Enter node and burn node : 2 234 16 643/-234
#       16       
#   2       234   
#             643 
# There is no -234 in the tree.

# Test Case 3
# Enter node and burn node : 1 2 3 4 5 6 7 8 9 0 10 11/0
#               4               
#       2               8       
#   1       3       6       10   
#                 5   7   9   11 
# 0
# 1
# 2
# 3 4
# 8 
# 6 10 
# 5 7 9 11 

# Test Case 4
# Enter node and burn node : -4 34 12 845 2 13 834 23 12 4 76 32 45 68/68
#                               13                               
#               12                               34               
#       2               12               23               834       
#   -4       4                               32       68       845   
#                                                 45   76         
# 68
# 45 76 834
# 845 34
# 23 13
# 32 12 
# 2 12 
# -4 4 

# Test Case 5
# Enter node and burn node : 6 5 3 21 45 687 87 3 2 1 234 54 24 78 34 0 342 1923 2468/87
#                               21                               
#               3                               87               
#       1               5               45               342       
#           2       3       6       24       54       234       1923   
#                                     34       78           687   2468 
# 87
# 45 342 21
# 24 54 234 1923 3 
# 34 78 687 2468 1 5 
# 0 2 3 6 

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None
        self.height = 1 

    def __str__(self):
        return str(self.data)


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root = self._insert(data, self.root)

    def _insert(self, data, root):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                root.left = self._insert(data, root.left)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                root.right = self._insert(data, root.right)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        return self._balance(data, root)

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right))+1
    def getcol(self,h):
        if h == 1:
            return 1
        return self.getcol(h-1) + self.getcol(h-1) + 1
    
    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _balance(self, data, node):
        balance_factor = self._balance_factor(node)

        if balance_factor > 1:
            if data < node.left.data:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance_factor < -1:
            if data > node.right.data:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root

    def printTree(self,M, root, col, row, height):
        if root is None:
            return
        M[row][col] = root.data
        self.printTree(M, root.left, col-pow(2, height-2), row+1, height-1)
        self.printTree(M, root.right, col+pow(2, height-2), row+1, height-1)
 
 
    def TreePrinter(self):
        h = self.height(self.root)
        col = self.getcol(h)
        M = [[0 for _ in range(col)] for __ in range(h)]
        self.printTree(M, self.root, col//2, 0, h)
        for i in M:
            for j in i:
                if j == 0:
                    print(" ", end=" ")
                else:
                    print(j, end=" ")
            print("")

    def findNode(self, data, node):
        if data == node.data:
            return [node, node.left, node.right]
        elif node.left == node.right == None or node == None:
            return False
        elif node.left and data == node.left.data:
            return [node.left, node.left.left, node.left.right, node]
        elif node.right and data == node.right.data:
            return [node.right, node.right.left, node.right.right, node]
        else:
            if data < node.data:
                return self.findNode(data, node.left)
            else:
                return self.findNode(data, node.right)


class Queue:
    def __init__(self) -> None:
        self.items = []

    def enQueue(self, item):
        self.items.append(item)

    def deQueue(self):
        return self.items.pop(0)

tree = AVLTree()
burnNode = []
stepBurn = []
temp = []
check = True
again = 0
size = 1

q = Queue()

count = -1

data = input("Enter node and burn node : ").split()
for e in data[:-1]:
    size += 1
    tree.insert(int(e))
tree.insert(int(data[-1].split("/")[0]))

tree.TreePrinter()

startBurn = int(data[-1].split("/")[1])

if not tree.findNode(startBurn, tree.root):
    print(f"There is no {startBurn} in the tree.")
else:
    for i in range(size):
        if not check:
            count = 0
        temp = []
        if again > 1:
            for i in range(again - 1):
                if len(q.items) > 0:
                    startBurn = q.deQueue()
                for item in tree.findNode(startBurn, tree.root):
                    if item and item not in burnNode:
                        count += 1
                        temp.append(item.data)
                        burnNode.append(item)
                        q.enQueue(item.data)
            again = 0
        if len(q.items) > 0:
            startBurn = q.deQueue()
        for item in tree.findNode(startBurn, tree.root):
            if item and item not in burnNode:
                count += 1
                temp.append(item.data)
                burnNode.append(item)
                q.enQueue(item.data)
        if count > 1:
            again = count
            stepBurn.append(list(map(str, temp)))
            temp = []
        elif count <= 1 and temp != []:
            stepBurn.append(list(map(str, temp)))
        if check:
            q.deQueue()
        check = False
if len(stepBurn) != 0:
    print(stepBurn[0].pop(0))  
    for i in stepBurn:
        print(" ".join(i))  
