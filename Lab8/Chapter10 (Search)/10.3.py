# Chapter : 10 - item : 3 - Fun with hashing

# ให้น้องเขียน Hashing โดยมีการทำงานดังนี้
# 1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
# 2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
# 3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
# 4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)
# อธิบาย Input
# แบ่ง Data เป็น 2 ชุดด้วย /
#     -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
#     -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ

# Test Case 1
#  ***** Fun with hashing *****
# Enter Input : 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love
# #1	(1+1, I)
# #2	None
# #3	None
# ---------------------------
# collision number 1 at 0
# #1	(1+1, I)
# #2	(OnE, Love)
# #3	None
# ---------------------------
# collision number 1 at 0
# collision number 2 at 1
# Max of collisionChain
# #1	(1+1, I)
# #2	(OnE, Love)
# #3	None
# ---------------------------
# #1	(1+1, I)
# #2	(OnE, Love)
# #3	(#$ew2, KMITL)
# ---------------------------
# This table is full !!!!!!

# Test Case 2
#  ***** Fun with hashing *****
# Enter Input : 5 5/one Un,two Deux,three Trois,four Quatre,five Cinq,ten Dix,eleven Onze
# #1	None
# #2	None
# #3	(one, Un)
# #4	None
# #5	None
# ---------------------------
# #1	None
# #2	(two, Deux)
# #3	(one, Un)
# #4	None
# #5	None
# ---------------------------
# collision number 1 at 1
# collision number 2 at 2
# #1	(three, Trois)
# #2	(two, Deux)
# #3	(one, Un)
# #4	None
# #5	None
# ---------------------------
# #1	(three, Trois)
# #2	(two, Deux)
# #3	(one, Un)
# #4	None
# #5	(four, Quatre)
# ---------------------------
# collision number 1 at 1
# collision number 2 at 2
# collision number 3 at 0
# collision number 4 at 0
# collision number 5 at 2
# Max of collisionChain
# #1	(three, Trois)
# #2	(two, Deux)
# #3	(one, Un)
# #4	None
# #5	(four, Quatre)
# ---------------------------
# collision number 1 at 2
# #1	(three, Trois)
# #2	(two, Deux)
# #3	(one, Un)
# #4	(ten, Dix)
# #5	(four, Quatre)
# ---------------------------
# This table is full !!!!!!

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class HashTable:
    def __init__(self, size, maxCollision):
        self.size = size
        self.maxCollision = maxCollision
        self.table = [None] * size
        self.full_flag = False 

    def hashFunction(self, key):
        return sum([ord(c) for c in key]) % self.size
    
    def insert(self, key, value):
        index = self.hashFunction(key)
        collision = 0
        if self.table[index] is None:
            self.table[index] = Data(key, value)
        else:
            while self.table[index] is not None:
                collision += 1
                print(f"collision number {collision} at {index}")
                index = (self.hashFunction(key) + collision**2) % self.size
                if collision >= self.maxCollision:
                    print("Max of collisionChain")
                    return  
            self.table[index] = Data(key, value)

    def __str__(self):
        for i in range(self.size):
            if self.table[i] is None:
                print(f"#{i+1}\tNone")
            else:
                print(f"#{i+1}\t{self.table[i]}")
        return "---------------------------"

    def len(self):
        return len([i for i in self.table if i is not None])

print(" ***** Fun with hashing *****")
data = input("Enter Input : ").split("/")
size, maxCollision = map(int, data[0].split())
data = data[1].split(",")
table = HashTable(size, maxCollision)

for i in data:
    key, value = i.split()
    table.insert(key, value)
    print(table)
    if table.len() >= size and not table.full_flag:
        print("This table is full !!!!!!")
        exit() 
