# Chapter : 4 - item : 4 - Cafe

# ณ ร้านกาแฟแห่งหนึ่งมีบาริสต้า 2 คน จะมีลูกค้าเข้ามาในร้านเวลา (si) บาริสต้าจะทำกาแฟให้ลูกค้าแต่ละคนในเวลา (pi) ที่ต่างกัน ดังนั้นจะมีคนที่รอคิวอยู่ แสดงลำดับลูกค้าที่ได้กาแฟ และคนที่รอคิวเพื่อจะสั่งกาแฟนานที่สุดรอกี่นาที ถ้าไม่ต้องรอคิวเลยให้แสดง No waiting
# ตัวอย่างข้อมูลเข้า
# Log : 0,3/0,7/2,3/7,7/10,5/10,1
# คำอธิบาย
# ลูกค้าคนที่ 1 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 3 นาที 
# ลูกค้าคนที่ 2 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 7 นาที 
# ลูกค้าคนที่ 3 เข้ามาในเวลาที่ 2 และสั่งกาแฟที่ทำนาน 3 นาที 
# ลูกค้าคนที่ 4 เข้ามาในเวลาที่ 7 และสั่งกาแฟที่ทำนาน 7 นาที 
# ลูกค้าคนที่ 5 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 5 นาที 
# ลูกค้าคนที่ 6 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 1 นาที 
# ไทม์ไลน์
# เวลา(t)    เหตุการณ์
# 0    ลูกค้าคนที่ 1 และ 2 เข้ามาในร้านและสั่งกาแฟ
# 2    ลูกค้าคนที่ 3 เข้ามาในร้าน
# 3    ลูกค้าคนที่ 1 ได้กาแฟ ลูกค้าคนที่ 3 สั่งกาแฟหลังจากรอคิวไป 1 นาที
# 6    ลูกค้าคนที่ 3 ได้กาแฟ
# 7    ลูกค้าคนที่ 2 ได้กาแฟ ลูกค้าคนที่ 4 เข้ามาในร้านและสั่งกาแฟ
# 10    ลูกค้าคนที่ 5 และ 6 เข้ามาในร้าน ลูกค้าคนที่ 5 สั่งกาแฟ
# 14    ลูกค้าคนที่ 4 ได้กาแฟ ลูกค้าคนที่ 6 สั่งกาแฟหลังจากรอคิวไป 4 นาที
# 15    ลูกค้าคนที่ 5 และ 6 ได้กาแฟ
# ผลลัพธ์ 
# Time 3 customer 1 get coffee  
# Time 6 customer 3 get coffee  
# Time 7 customer 2 get coffee  
# Time 14 customer 4 get coffee  
# Time 15 customer 5 get coffee  
# Time 15 customer 6 get coffee  
# The customer who waited the longest is : 6
# The customer waited for 4 minutes

# Test Case 1
#  ***Cafe***
# Log : 0,3/0,7/2,3/7,7/10,5/10,1
# Time 3 customer 1 get coffee  
# Time 6 customer 3 get coffee  
# Time 7 customer 2 get coffee  
# Time 14 customer 4 get coffee  
# Time 15 customer 5 get coffee  
# Time 15 customer 6 get coffee  
# The customer who waited the longest is : 6
# The customer waited for 4 minutes

# Test Case 2
#  ***Cafe***
# Log : 0,1/1,1/2,1/3,1/4,1/5,1
# Time 1 customer 1 get coffee  
# Time 2 customer 2 get coffee  
# Time 3 customer 3 get coffee  
# Time 4 customer 4 get coffee  
# Time 5 customer 5 get coffee  
# Time 6 customer 6 get coffee  
# No waiting

# Test Case 3
#  ***Cafe***
# Log : 0,1/0,1/1,1/1,1/2,1/2,1
# Time 1 customer 1 get coffee  
# Time 1 customer 2 get coffee  
# Time 2 customer 3 get coffee  
# Time 2 customer 4 get coffee  
# Time 3 customer 5 get coffee  
# Time 3 customer 6 get coffee  
# No waiting

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

def cafe(log):
    log_queue = Queue()
    main = Queue()
    barista1 = None
    barista2 = None
    main_time = 0
    time1 = 0
    time2 = 0
    longest_wait = 0
    longest_wait_customer = None
    wait_times = {}

    for idx, entry in enumerate(log):
        entry.append(idx + 1)  
        log_queue.enQueue(entry)

    while not log_queue.isEmpty() or not main.isEmpty() or barista1 or barista2:
        barista1_done = None
        barista2_done = None

        while not log_queue.isEmpty() and int(log_queue.peek()[0]) == main_time:
            customer = log_queue.deQueue()
            main.enQueue(customer)
            wait_times[customer[2]] = main_time
        
        if barista1:
            time1 -= 1
            if time1 == 0:
                barista1_done = barista1
                barista1 = None

        if barista2:
            time2 -= 1
            if time2 == 0:
                barista2_done = barista2
                barista2 = None
        
        done_customers = []
        if barista1_done:
            done_customers.append((barista1_done[2], main_time))
        if barista2_done:
            done_customers.append((barista2_done[2], main_time))
        
        done_customers.sort()
        
        for customer_id, time in done_customers:
            print(f"Time {time} customer {customer_id} get coffee")
        
        if not barista1 and not main.isEmpty():
            barista1 = main.deQueue()
            wait_time = main_time - wait_times[barista1[2]]
            wait_times[barista1[2]] = wait_time
            if wait_time > longest_wait:
                longest_wait = wait_time
                longest_wait_customer = barista1[2]
            time1 = int(barista1[1])
        
        if not barista2 and not main.isEmpty():
            barista2 = main.deQueue()
            wait_time = main_time - wait_times[barista2[2]]
            wait_times[barista2[2]] = wait_time
            if wait_time > longest_wait:
                longest_wait = wait_time
                longest_wait_customer = barista2[2]
            time2 = int(barista2[1])

        main_time += 1
    
    if longest_wait == 0:
        print("No waiting")
    else:
        print(f"The customer who waited the longest is : {longest_wait_customer}")
        print(f"The customer waited for {longest_wait} minutes")

print(" ***Cafe***")
log = input("Log : ").split('/')
log = [i.split(',') for i in log]
cafe(log)