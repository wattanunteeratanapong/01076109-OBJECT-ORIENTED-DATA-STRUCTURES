# Chapter : 3 - item : 2 - Parenthesis Matching

# จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา
# โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด
# 1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด
# 2. วงเล็บปิดเกิน
# 3. วงเล็บเปิดเกิน
# แล้วให้แสดงผลตามตัวอย่าง

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
    
stack = Stack()
str = input("Enter expresion : ")

filter_str = "".join([i for i in str if i in "()[]{}"])

for i in filter_str:
    if i in "([{":
        stack.push(i)
    elif i in ")]}":
        if stack.isEmpty():
            print(f"{str} close paren excess")
            exit()
        top = stack.pop()
        if i == ")" and top != "(":
            print(f"{str} Unmatch open-close")
            exit()
        elif i == "]" and top != "[":
            print(f"{str} Unmatch open-close")
            exit()
        elif i == "}" and top != "{":
            print(f"{str} Unmatch open-close")
            exit()

if not stack.isEmpty():
    print(f"{str} open paren excess   {len(stack.stack)} : {''.join(stack.stack)}")
else:
    print(f"{str} MATCH")

# Time Complexity
# O(n)

# Space Complexity
# O(n)