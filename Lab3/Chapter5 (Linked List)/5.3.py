# Chapter : 5 - item : 3 - Arthur กับเมืองลี้ลับ

# Arthur เป็นเด็กหนุ่มผู้หลงใหลในการเขียนโปรแกรมและการแก้ปริศนา หนึ่งวันหนึ่ง เขาได้รับ จดหมายลึกลับที่บอกว่าเขาถูกเชิญให้ไปที่เมืองปริศนา ซึ่งเป็นเมืองที่ถูกสร้างขึ้นมาจากโครงสร้างข้อมูล แบบ Linked List ทั้งหมด
# เมื่อ Arthur มาถึงเมืองปริศนา เขาพบว่าที่นี่มีการจัดการแข่งขันเขียนโปรแกรม โดยมีเป้าหมายคือ การแก้ปริศนาและช่วยเหลือผู้อยู่อาศัยในเมืองปริศนาให้พ้นจากปัญหาต่างๆ ที่เกิดขึ้นจากโครงสร้าง ข้อมูลที่ซับซ้อน Arthur ได้รับภารกิจแรกคือการแก้ปัญหาการจัดเรียงข้อมูลใน Linked List เพื่อทำให้ข้อมูลเรียงลำดับถูกต้อง
# ระดับความยาก : ง่ายคดๆ
# หมายเหตุ:
# - หลักการจัดวางคือ ตัวเลข, ตัวอักษรพิมพ์ใหญ่, ตัวอักษรพิมพ์เล็ก (คุ้นๆไหมมันคืออะไร?)
# - ไม่อนุญาตให้ใช้ .sort() เพราะตรวจ code นะจ๊ะ

# Test Case 1
# Enter unsorted Linked List: 5 4 3 2 1 0
# Before: 5 -> 4 -> 3 -> 2 -> 1 -> 0
# After : 0 -> 1 -> 2 -> 3 -> 4 -> 5

# Test Case 2
# Enter unsorted Linked List: 9 3 2 90 2 -1 3 8 2 3
# Before: 9 -> 3 -> 2 -> 90 -> 2 -> -1 -> 3 -> 8 -> 2 -> 3
# After : -1 -> 2 -> 2 -> 2 -> 3 -> 3 -> 3 -> 8 -> 9 -> 90

# Test Case 3
# Enter unsorted Linked List: z x y a c b
# Before: z -> x -> y -> a -> c -> b
# After : a -> b -> c -> x -> y -> z

# Test Case 4
# Enter unsorted Linked List: A g W Z b a P Q Y i l
# Before: A -> g -> W -> Z -> b -> a -> P -> Q -> Y -> i -> l
# After : A -> P -> Q -> W -> Y -> Z -> a -> b -> g -> i -> l

# Test Case 5
# Enter unsorted Linked List: settle nationalism note technique persist herd sculpture heat flatware jury
# Before: settle -> nationalism -> note -> technique -> persist -> herd -> sculpture -> heat -> flatware -> jury
# After : flatware -> heat -> herd -> jury -> nationalism -> note -> persist -> sculpture -> settle -> technique

class Node:
    def __init__(self, value, index):
        self.value = value
        self.next = None
        self.index = index

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def append(self, value):
        new_node = Node(value, self.length)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def get_prev(self, node):
        current_node = self.head
        while current_node is not None and current_node.next is not node:
            current_node = current_node.next
        return current_node

    def shuffle(self, cur, next):
        if self.head == cur:
            cur.next = next.next
            next.next = cur
            self.head = next
            if cur.next is None:
                self.tail = cur
        elif self.tail == next:
            prev = self.get_prev(cur)
            prev.next = next
            next.next = cur
            cur.next = None
            self.tail = cur
        else:
            prev = self.get_prev(cur)
            very_next = next.next
            prev.next = next
            next.next = cur
            cur.next = very_next

    def size(self):
        return self.length

    def __str__(self):
        if self.isEmpty():
            return "Linked List is Empty"
        else:
            current_node = self.head
            result = ""
            while current_node is not None:
                result += str(current_node.value)
                if current_node.next is not None:
                    result += " -> "
                current_node = current_node.next
            return result

    def sort(self):
        def compare(a, b):
            a, b = str(a), str(b)
            
            def is_numeric(s):
                try:
                    float(s)
                    return True
                except ValueError:
                    return False
            
            if is_numeric(a) and is_numeric(b):
                return float(a) > float(b)
            if is_numeric(a):
                return False
            if is_numeric(b):
                return True

            if a.isupper() and b.isupper():
                return a > b
            if a.islower() and b.islower():
                return a > b
            if a.isupper() and b.islower():
                return False
            if a.islower() and b.isupper():
                return True

            return a.lower() > b.lower()

        for i in range(self.size()):
            current_node = self.head
            for j in range(self.size() - 1):
                if compare(current_node.value, current_node.next.value):
                    self.shuffle(current_node, current_node.next)
                else:
                    current_node = current_node.next

Unsorted = SinglyLinkedList()
text_input = input("Enter unsorted Linked List: ").split()
        
for i in text_input:
    try:
        Unsorted.append(int(i))
    except ValueError:
        Unsorted.append(i)
print("Before:", Unsorted)

Unsorted.sort()
print("After :", Unsorted)
