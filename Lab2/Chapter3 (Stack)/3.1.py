# Chapter : 3 - item : 1 - สร้าง stack

# ให้นักศึกษา สร้าง class Stack ด้วย list ของ python โดย มี method ดังต่อไปนี้
# def __init__()    // ใช้สำหรับสร้าง list ว่าง
# def push(i)        // เก็บข้อมูลลง stack
# def pop()          // นำข้อมูลออกจาก stack
# def isEmpty()   // ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
# def size()         // ตรวจสอบจำนวนข้อมูลใจ stack

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
        
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)
    
print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]
s = Stack()
for e in ls:
    s.push(e)
print(s.size(), "Data in stack:", s.stack)
while not s.isEmpty():
    s.pop()
print(s.size(), "Data in stack:", s.stack)

# Time Complexity
# O(n)

# Space Complexity
# O(n)