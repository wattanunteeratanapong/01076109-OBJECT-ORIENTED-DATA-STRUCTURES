# Chapter : 4 - item : 3 - Secret Message

# จงเขียน ฟังก์ชั่นสำหรับการ encode และ decode ของ String ที่รับมาโดยให้ทำเป็นรูปแบบ Queue
# รูปแบบการรับ Input โดยจะคั่นแต่ละตำแหน่งด้วย คอมม่า(',') :
#     - ตำแหน่งที่หนึ่ง string ไม่จำกัดความยาวโดยที่จะไม่นับช่องว่าง(spacebar)
#     - ตำแหน่งที่สอง ชุดตัวเลข(1-9)
# โดยที่รูปแบบการ encode คือ การนำ String ที่รับมาเพิ่มค่า ascii เท่ากับค่าของชุดตัวเลขในตำแหน่งแรก หลังจากนั้นให้ dequeue ชุดตัวเลขออกไปไว้ข้างหลังสุด เช่น ตัวอักษรตำแหน่งแรกคือ i และชุดตัวเลขในตำแหน่งแรกคือ 2 ดังนั้นตัวอักษรที่ได้จากการ encode คือ k โดยจะทำการวนชุดตัวเลขไปเรื่อยๆจนกระทั่งทำการ encode ทุกตัวอักษรใน String ครบ ถ้าหากผลลัพธ์จากการเพิ่มหรือลดค่า ascii ไม่ใช่ตัวอักษรให้กลับมาวนในชุดตัวอักษร เช่น อักษร z ทำการ encode ด้วยเลข 2 จะได้ b และหากทำการ decode ตัวอักษร A ด้วย 2 จะได้ Y 
# โดยการ decode หลังจาก encode ต้องให้คำตอบที่มีค่าเท่ากับ String เดิมก่อนทำการ encode 
# ***ให้ใช้วิธี enqueue และ dequeue ในการเลื่อนตำแหน่ง เท่านั้น***
# โดยรูปแบบการ run ดังนี้ :
# q1 = Queue(string)
# q2 = Queue(number)
# encodemsg(q1, q2)
# decodemsg(q1, q2)

class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enQueue(self, data):
        self.queue.append(data)

    def deQueue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return None
        
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)
    
def encodemsg(q1, q2):
    decode_message = q1.queue.copy()
    for i in range(q1.size()):
        char = q1.queue[i]
        shift = int(q2.queue[0])
        if char.isupper():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        q1.queue[i] = new_char
        q2.enQueue(q2.deQueue())
    print(f"Encode message is :  {q1.queue}")
    print(f"Decode message is :  {decode_message}")

q1 = Queue()
q2 = Queue()
text_input = input("Enter String and Code : ").split(',')
string = []
code = text_input[1]

for i in text_input[0]:
    if i.isalpha():
        string.append(i)

for i in string:
    q1.enQueue(i)

for i in code:
    q2.enQueue(i)

encodemsg(q1, q2)

# Time Complexity
# O(n)

# Space Complexity
# O(n)