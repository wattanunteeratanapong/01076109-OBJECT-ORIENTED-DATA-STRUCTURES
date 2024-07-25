# Chapter : 3 - item : 3 - Postfix Calculator

# จงเขียนโปรแกรมโดยใช้ Stack เพื่อคำนวณหา ค่าของนิพจน์แบบ postfix 
# โดยให้แสดงผลลัพธ์ตามตัวอย่าง

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
    
def postFixeval(st):
    s = Stack()
    for i in st:
        try:
            num = float(i)
            s.push(num)
        except ValueError:
            if i in "+-*/":
                b = s.pop()
                a = s.pop()
                if i == "+":
                    s.push(a + b)
                elif i == "-":
                    s.push(a - b)
                elif i == "*":
                    s.push(a * b)
                elif i == "/":
                    s.push(a / b)
    return s.pop()

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())
print("Answer : ", '{:.2f}'.format(postFixeval(token)))

# Time Complexity
# O(n)

# Space Complexity
# O(n)