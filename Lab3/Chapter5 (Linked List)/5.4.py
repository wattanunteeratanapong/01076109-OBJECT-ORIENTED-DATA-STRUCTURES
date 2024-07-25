# Chapter : 5 - item : 4 - VIM Text Editor

# กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor
# ***** อธิบาย Input 5 แบบ *****
# 1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป
# 2.  L              :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร
# 3.  R             :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร
# 4.  B             :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร
# 5.  D             :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

# Test Case 1
# Enter Input : I Apple,I Bird,I Cat
# Apple Bird Cat | 

# Test Case 2
# Enter Input : I Apple,I Bird,I Cat,L
# Apple Bird | Cat 

# Test Case 3
# Enter Input : I Apple,I Bird,I Cat,L,L
# Apple | Bird Cat 

# Test Case 4
# Enter Input : I Apple,I Bird,I Cat,L,L,L,L,L
# | Apple Bird Cat 

# Test Case 5
# Enter Input : I Apple,I Bird,I Cat,L,L,R
# Apple Bird | Cat 

# Test Case 6
# Enter Input : I Apple,I Bird,I Cat,L,L,R,B
# Apple | Cat 

# Test Case 7
# Enter Input : I Apple,I Bird,L,L,R,D,D
# Apple | 

# Test Case 8
# Enter Input : L,R,I ABC,I DE,L,I FGHI
# ABC FGHI | DE 

# Test Case 9
# Enter Input : I A,I B,L,L,R,D,D,L,L,R,I BCD,L,L,B,D,R,R,L,L
# | BCD 

# Test Case 10
# Enter Input : I I,I KMITL,L,L,R,I Love
# I Love | KMITL 

# Test Case 11
# Enter Input : I I,I KMITL,L,L,R,I Love,D,I DataStructure,L,L,R,L,R,B,I Hate
# I Hate | DataStructure 

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            
    def delete_start(self):
        if self.head is None:
            return
        self.head = self.head.next
        
    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        
    def delete_at_index(self, idx):
        if self.head is None:
            return
        if idx == 0:
            self.head = self.head.next
            return
        temp = self.head
        count = 0
        while temp is not None:
            if count == idx - 1 and temp.next is not None:
                temp.next = temp.next.next
                return
            temp = temp.next
            count += 1

    def add_after_index(self, idx, data):
        new_node = Node(data)
        temp = self.head 
        count = 0
        while temp is not None:
            if count == idx: 
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            count += 1
            
    def add_before_index(self, idx, data):
        if idx == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        new_node = Node(data)
        temp = self.head
        count = 0
        while temp is not None:
            if count == idx - 1:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            count += 1
            
    def find_index_by_value(self, data):
        temp = self.head
        count = 0
        while temp is not None:
            if temp.data == data:
                return count
            count += 1
            temp = temp.next
        return -1
    
    def find_value_by_index(self, idx):
        temp = self.head
        count = 0
        while temp is not None:
            if count == idx:
                return temp.data
            count += 1
            temp = temp.next
        return None
    
    def count_elements(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count
            
    def __str__(self):
        temp = self.head
        elements = []
        while temp is not None:
            elements.append(str(temp.data))
            temp = temp.next
        return " ".join(elements)

def vim_text_editor(commands):
    initial = Node("|")
    linked_list = SinglyLinkedList(initial)
    
    for cmd in commands:
        parts = cmd.strip().split(" ")
        action = parts[0]
        text = str(parts[1]) if len(parts) > 1 else None
        
        cursor_position = linked_list.find_index_by_value("|")
        
        if action == "I":
            linked_list.add_after_index(cursor_position, text)
            linked_list.delete_at_index(cursor_position)
            linked_list.add_after_index(cursor_position, "|")
            
        elif action == "L":
            if cursor_position > 0:
                linked_list.delete_at_index(cursor_position)
                linked_list.add_before_index(cursor_position - 1, "|")
                
        elif action == "R":
            if cursor_position < linked_list.count_elements() - 1:
                linked_list.delete_at_index(cursor_position)
                linked_list.add_after_index(cursor_position, "|")
                
        elif action == "B":
            if cursor_position > 0:
                linked_list.delete_at_index(cursor_position - 1)
                
        elif action == "D":
            if cursor_position < linked_list.count_elements() - 1:
                linked_list.delete_at_index(cursor_position + 1)
                
    print(linked_list)

commands = input("Enter Input : ").strip().split(",")
vim_text_editor(commands)
