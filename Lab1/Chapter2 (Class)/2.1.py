# Chapter : 2 - item : 1 - Simple OOP Calculator

# จงเขียน Overloading Function สำหรับ Calculator class โดยที่มีรูปแบบ Code ดังนี้ (สามารถเพิ่มพารามิเตอร์ได้)

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        sum = self.num1 + self.num2
        return sum 

    def sub(self):
        sub = self.num1 - self.num2
        return sub

    def mul(self):
        multi = self.num1 * self.num2
        return multi

    def div(self):
        divide = self.num1 / self.num2
        return divide

x, y = input("Enter num1 num2 : ").split(",")
calculator = Calculator(int(x), int(y))

print(calculator.add())
print(calculator.sub())
print(calculator.mul())
print(calculator.div())

# Time Complexity
# O(1)

# Space Complexity
# O(1)