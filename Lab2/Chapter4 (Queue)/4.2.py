# Chapter : 4 - item : 2 - แถวคอย
 
# จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue
# โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้
# แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ
# แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ
# ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2
# จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2]

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
    
def simulate_queue(customers, time):
    main_queue = Queue()
    cashier1 = Queue()
    cashier2 = Queue()
    
    for customer in customers:
        main_queue.enQueue(customer)
    
    cashier1_timer = 1
    cashier2_timer = 1

    for minute in range(1, time + 1):
        # Process customers at cashier 1
        if not cashier1.isEmpty():
            if cashier1_timer == 3:
                cashier1.deQueue()
                cashier1_timer = 0
            cashier1_timer += 1

        # Process customers at cashier 2
        if not cashier2.isEmpty():
            if cashier2_timer == 2:
                cashier2.deQueue()
                cashier2_timer = 0
            cashier2_timer += 1

        # Move customers from the main queue to cashier queues
        if not main_queue.isEmpty():
            if cashier1.size() < 5:
                cashier1.enQueue(main_queue.deQueue())
            elif cashier2.size() < 5:
                cashier2.enQueue(main_queue.deQueue())

        print(minute, list(main_queue.queue), list(cashier1.queue), list(cashier2.queue))

# Enter people and time : HELLO_WORLD 13
input_data = input("Enter people and time : ").split()
customer = list(input_data[0])
time = int(input_data[1])

simulate_queue(customer, time)

# Time Complexity
# O(n)

# Space Complexity
# O(n)