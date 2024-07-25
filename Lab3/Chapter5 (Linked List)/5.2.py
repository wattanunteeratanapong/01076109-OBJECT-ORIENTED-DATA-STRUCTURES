class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next is not None:
            cur = cur.next
            s += str(cur.value) + " "
        return s.strip()

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.prev is not None:
            cur = cur.prev
            s += str(cur.value) + " "
        return s.strip()

    def isEmpty(self):
        return self.head is None

    def append(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def addHead(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert(self, index, value):
        new_node = Node(value)
        list_size = self.size()
        if index < 0:
            index += list_size
        if index <= 0:
            self.addHead(value)
        elif index >= list_size:
            self.append(value)
        else:
            current_node = self.head
            for _ in range(index - 1):  
                current_node = current_node.next
            new_node.next = current_node.next
            if current_node.next:  
                current_node.next.prev = new_node
            new_node.prev = current_node
            current_node.next = new_node



    def search(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return "Found"
            cur = cur.next
        return "Not Found"

    def index(self, value):
        cur = self.head
        idx = 0
        while cur is not None:
            if cur.value == value:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def size(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def pop(self, pos):
        if pos < 0 or pos >= self.size():
            return "Out of Range"
        if pos == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif pos == self.size() - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            cur = self.head
            for _ in range(pos):
                cur = cur.next
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        return "Success"

L = DoublyLinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1} -> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())