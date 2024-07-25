# Chapter : 4 - item : 1 - รู้จักกับ QUEUE

# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา
# E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผล Size ปัจจุบันของ QUEUE
# D                 ให้ทำการแสดงผลของvalueที่อยู่หน้าสุดและindexของvalueนั้นจากนั้นทำการ De_QUEUE ถ้าหากไม่มี value อยู่ใน Queue ให้แสดงผลเป็น  -1
# *** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

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

list = input("Enter Input : ").split(',')
queue = Queue()

for i in list:
    j = i.split()
    state = j[0]
    if state == "E":
        queue.enQueue(j[1])
        print(queue.size())
    elif state == "D":
        dequeued = queue.deQueue()
        if dequeued is not None:
            print(f"{dequeued} 0")
        else:
            print(-1)

if queue.isEmpty()==False:
    print(" ".join(queue.queue))
if queue.isEmpty()==True:
    print("Empty")

# Time Complexity
# O(n)

# Space Complexity
# O(n)