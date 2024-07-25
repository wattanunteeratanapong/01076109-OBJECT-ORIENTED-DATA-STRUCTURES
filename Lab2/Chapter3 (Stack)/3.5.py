# Chapter : 3 - item : 5 - วันหนึ่งฉันเดินเข้าป่า (2) a.k.a Into the Woods but หลอนประสาท

# <<<  กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก (เดินยังไงให้หลงครับเนี่ยย - -") หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป >>>
# ****  ด้านบนจะเป็นเนื้อหาของ  < วันหนึ่งฉันเดินเข้าป่า   version  1 >  เผื่อน้องบางคน Random ไม่ได้ครับ
# หลังจากกฤษฎาเดินหลงป่ามาได้สักพักก็ได้ไปเจอเห็ดสีสันสวยงามจึงได้หยิบขึ้นมากิน  หลังจากกินเข้าไปทำให้กฤษฎามีอาการแปลกๆเกิดขึ้น  เนื่องจากเห็ดที่กินเข้าไปเป็นเห็ดพิษ  แต่กฤษฎาก็ยังคอยนับความสูงต้นไม้ไปเรื่อยๆเหมือนเดิม  ผลข้างเคียงจากเห็ดพิษก็ได้ส่งผลกระทบต่อการนับต้นไม้ของกฤษฎาเนื่องจากอาการหลอนประสาท ทำให้ต้นไม้ที่มีความสูงเป็นเลขคี่มีการเพิ่มความสูงมา 2 เมตร และต้นไม้เลขคู่ลดความสูงไป  1 เมตร ความสูงที่น้อยที่สุดคือ 1 เมตร
# ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น
# อธิบาย Input :  A  <Heights>  แสดงถึงความสูงของต้นไม้  ,  B  คือการหันหลังกลับมามอง , S  คือการโดนผลกระทบจากเห็ดพิษ
# อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 
# โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง

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
    
def count_visible_trees(stack):
    if stack.isEmpty():
        return 0
    visible_count = 0
    max_height = 0
    temp_stack = Stack()

    while not stack.isEmpty():
        height = stack.pop()
        temp_stack.push(height)
        if height > max_height:
            visible_count += 1
            max_height = height
    
    while not temp_stack.isEmpty():
        stack.push(temp_stack.pop())
    
    return visible_count

def process_heights(stack):
    for i in range(len(stack.stack)):
        if stack.stack[i] % 2 == 0:
            stack.stack[i] = max(1, stack.stack[i] - 1)  
        else: 
            stack.stack[i] += 2  

input_data = input("Enter Input : ").split(",")

stack = Stack()
temp_stack = []

for command in input_data:
    if command.startswith('A '):
        height = int(command.split()[1])
        stack.push(height)
    elif command == 'B':
        print(count_visible_trees(stack))
    elif command == 'S':
        process_heights(stack)

# Time Complexity
# O(n)

# Space Complexity
# O(n)