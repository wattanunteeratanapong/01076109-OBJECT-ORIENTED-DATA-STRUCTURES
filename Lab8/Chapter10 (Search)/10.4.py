# Chapter : 10 - item : 4 - Rehashing

# ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
# 1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
# 2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด
# หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11
# การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision
# อธิบาย Input
# แบ่ง Data เป็น 2 ชุดด้วย /
#     -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
#     -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด

# Test Case 1
#  ***** Rehashing *****
# Enter Input : 5 1 67/1 6
# Initial Table :
# #1	None
# #2	None
# #3	None
# #4	None
# #5	None
# ----------------------------------------
# Add : 1
# #1	None
# #2	1
# #3	None
# #4	None
# #5	None
# ----------------------------------------
# Add : 6
# collision number 1 at 1
# ****** Max collision - Rehash !!! ******
# #1	None
# #2	1
# #3	None
# #4	None
# #5	None
# #6	None
# #7	6
# #8	None
# #9	None
# #10	None
# #11	None
# ----------------------------------------

# Test Case 2
#  ***** Rehashing *****
# Enter Input : 5 1 10/1 6
# Initial Table :
# #1	None
# #2	None
# #3	None
# #4	None
# #5	None
# ----------------------------------------
# Add : 1
# ****** Data over threshold - Rehash !!! ******
# #1	None
# #2	1
# #3	None
# #4	None
# #5	None
# #6	None
# #7	None
# #8	None
# #9	None
# #10	None
# #11	None
# ----------------------------------------
# Add : 6
# ****** Data over threshold - Rehash !!! ******
# #1	None
# #2	1
# #3	None
# #4	None
# #5	None
# #6	None
# #7	6
# #8	None
# #9	None
# #10	None
# #11	None
# #12	None
# #13	None
# #14	None
# #15	None
# #16	None
# #17	None
# #18	None
# #19	None
# #20	None
# #21	None
# #22	None
# #23	None
# ----------------------------------------

# Test Case 3
#  ***** Rehashing *****
# Enter Input : 5 1 10/0 1 6 20
# Initial Table :
# #1	None
# #2	None
# #3	None
# #4	None
# #5	None
# ----------------------------------------
# Add : 0
# ****** Data over threshold - Rehash !!! ******
# #1	0
# #2	None
# #3	None
# #4	None
# #5	None
# #6	None
# #7	None
# #8	None
# #9	None
# #10	None
# #11	None
# ----------------------------------------
# Add : 1
# ****** Data over threshold - Rehash !!! ******
# #1	0
# #2	1
# #3	None
# #4	None
# #5	None
# #6	None
# #7	None
# #8	None
# #9	None
# #10	None
# #11	None
# #12	None
# #13	None
# #14	None
# #15	None
# #16	None
# #17	None
# #18	None
# #19	None
# #20	None
# #21	None
# #22	None
# #23	None
# ----------------------------------------
# Add : 6
# ****** Data over threshold - Rehash !!! ******
# #1	0
# #2	1
# #3	None
# #4	None
# #5	None
# #6	None
# #7	6
# #8	None
# #9	None
# #10	None
# #11	None
# #12	None
# #13	None
# #14	None
# #15	None
# #16	None
# #17	None
# #18	None
# #19	None
# #20	None
# #21	None
# #22	None
# #23	None
# #24	None
# #25	None
# #26	None
# #27	None
# #28	None
# #29	None
# #30	None
# #31	None
# #32	None
# #33	None
# #34	None
# #35	None
# #36	None
# #37	None
# #38	None
# #39	None
# #40	None
# #41	None
# #42	None
# #43	None
# #44	None
# #45	None
# #46	None
# #47	None
# ----------------------------------------
# Add : 20
# #1	0
# #2	1
# #3	None
# #4	None
# #5	None
# #6	None
# #7	6
# #8	None
# #9	None
# #10	None
# #11	None
# #12	None
# #13	None
# #14	None
# #15	None
# #16	None
# #17	None
# #18	None
# #19	None
# #20	None
# #21	20
# #22	None
# #23	None
# #24	None
# #25	None
# #26	None
# #27	None
# #28	None
# #29	None
# #30	None
# #31	None
# #32	None
# #33	None
# #34	None
# #35	None
# #36	None
# #37	None
# #38	None
# #39	None
# #40	None
# #41	None
# #42	None
# #43	None
# #44	None
# #45	None
# #46	None
# #47	None
# ----------------------------------------

# Test Case 4
#  ***** Rehashing *****
# Enter Input : 7 6 70/13 15 6 24 23
# Initial Table :
# #1	None
# #2	None
# #3	None
# #4	None
# #5	None
# #6	None
# #7	None
# ----------------------------------------
# Add : 13
# #1	None
# #2	None
# #3	None
# #4	None
# #5	None
# #6	None
# #7	13
# ----------------------------------------
# Add : 15
# #1	None
# #2	15
# #3	None
# #4	None
# #5	None
# #6	None
# #7	13
# ----------------------------------------
# Add : 6
# collision number 1 at 6
# #1	6
# #2	15
# #3	None
# #4	None
# #5	None
# #6	None
# #7	13
# ----------------------------------------
# Add : 24
# #1	6
# #2	15
# #3	None
# #4	24
# #5	None
# #6	None
# #7	13
# ----------------------------------------
# Add : 23
# ****** Data over threshold - Rehash !!! ******
# collision number 1 at 6
# collision number 2 at 7
# #1	None
# #2	None
# #3	None
# #4	None
# #5	None
# #6	None
# #7	6
# #8	24
# #9	None
# #10	None
# #11	23
# #12	None
# #13	None
# #14	13
# #15	None
# #16	15
# #17	None
# ----------------------------------------

# Test Case 5
#  ***** Rehashing *****
# Enter Input : 19 2 49/8741 4874 787842 77 8789 7542 751213 978458
# Initial Table :
# #1	None
# #2	None
# #3	None
# #4	None
# #5	None
# #6	None
# #7	None
# #8	None
# #9	None
# #10	None
# #11	None
# #12	None
# #13	None
# #14	None
# #15	None
# #16	None
# #17	None
# #18	None
# #19	None
# ----------------------------------------
# Add : 8741
# #1	None
# #2	8741
# #3	None
# #4	None
# #5	None
# #6	None
# #7	None
# #8	None
# #9	None
# #10	None
# #11	None
# #12	None
# #13	None
# #14	None
# #15	None
# #16	None
# #17	None
# #18	None
# #19	None
# ----------------------------------------
# Add : 4874
# #1	None
# #2	8741
# #3	None
# #4	None
# #5	None
# #6	None
# #7	None
# #8	None
# #9	None
# #10	None
# #11	4874
# #12	None
# #13	None
# #14	None
# #15	None
# #16	None
# #17	None
# #18	None
# #19	None
# ----------------------------------------
# Add : 787842
# #1	None
# #2	8741
# #3	None
# #4	None
# #5	None
# #6	None
# #7	None
# #8	787842
# #9	None
# #10	None
# #11	4874
# #12	None
# #13	None
# #14	None
# #15	None
# #16	None
# #17	None
# #18	None
# #19	None
# ----------------------------------------
# Add : 77
# collision number 1 at 1
# #1	None
# #2	8741
# #3	77
# #4	None
# #5	None
# #6	None
# #7	None
# #8	787842
# #9	None
# #10	None
# #11	4874
# #12	None
# #13	None
# #14	None
# #15	None
# #16	None
# #17	None
# #18	None
# #19	None
# ----------------------------------------
# Add : 8789
# #1	None
# #2	8741
# #3	77
# #4	None
# #5	None
# #6	None
# #7	None
# #8	787842
# #9	None
# #10	None
# #11	4874
# #12	8789
# #13	None
# #14	None
# #15	None
# #16	None
# #17	None
# #18	None
# #19	None
# ----------------------------------------
# Add : 7542
# #1	None
# #2	8741
# #3	77
# #4	None
# #5	None
# #6	None
# #7	None
# #8	787842
# #9	None
# #10	None
# #11	4874
# #12	8789
# #13	None
# #14	None
# #15	None
# #16	None
# #17	None
# #18	None
# #19	7542
# ----------------------------------------
# Add : 751213
# collision number 1 at 10
# collision number 2 at 11
# ****** Max collision - Rehash !!! ******
# collision number 1 at 36
# #1	None
# #2	None
# #3	None
# #4	None
# #5	None
# #6	None
# #7	None
# #8	None
# #9	8741
# #10	None
# #11	None
# #12	751213
# #13	None
# #14	None
# #15	None
# #16	8789
# #17	None
# #18	None
# #19	None
# #20	None
# #21	None
# #22	None
# #23	None
# #24	None
# #25	None
# #26	None
# #27	None
# #28	787842
# #29	None
# #30	None
# #31	None
# #32	None
# #33	None
# #34	None
# #35	None
# #36	None
# #37	4874
# #38	77
# #39	None
# #40	7542
# #41	None
# ----------------------------------------
# Add : 978458
# #1	None
# #2	None
# #3	None
# #4	None
# #5	None
# #6	None
# #7	None
# #8	None
# #9	8741
# #10	None
# #11	None
# #12	751213
# #13	None
# #14	None
# #15	None
# #16	8789
# #17	None
# #18	None
# #19	None
# #20	None
# #21	None
# #22	None
# #23	None
# #24	None
# #25	None
# #26	None
# #27	None
# #28	787842
# #29	None
# #30	None
# #31	None
# #32	None
# #33	None
# #34	None
# #35	978458
# #36	None
# #37	4874
# #38	77
# #39	None
# #40	7542
# #41	None
# ----------------------------------------

class HashTable:
    def __init__(self, size, max_col, threshold):
        self.size = size
        self.max_col = max_col
        self.threshold = threshold
        self.table = [None] * size
        self.data_count = 0
        self.add_list = set()

    def insert(self, key):
        index = key % self.size
        init_index = index
        col = 0

        while col < self.max_col:
            if self.table[index] is None:
                self.table[index] = key
                self.data_count += 1
                self.add_list.add(key)
                return True
            else:
                col += 1
                print(f"collision number {col} at {index}")
                if col >= self.max_col:
                    print("****** Max collision - Rehash !!! ******")
                    return False
                index = (init_index + col ** 2) % self.size
        return False

    def is_over(self):
        percent = (self.data_count + 1) / self.size * 100
        if percent >= self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            return True
        return False

    def rehash(self):
        self.size = self.get_prime(self.size * 2)
        self.table = [None] * self.size
        self.data_count = 0
        for key in self.add_list:
            self.insert(key)

    def get_prime(self, n):
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        prime = n
        while True:
            if is_prime(prime):
                return prime
            prime += 1

    def print_table(self):
        for i in range(self.size):
            value = self.table[i]
            print(f"#{i + 1}\t{value if value is not None else 'None'}")
        print("----------------------------------------")

    def add_data(self, key):
        print(f"Add : {key}")
        if self.is_over():
            self.rehash()
        inserted = self.insert(key)
        if not inserted:
            self.rehash()
            self.insert(key)
        self.print_table()



print(" ***** Rehashing *****")
inp = input("Enter Input : ").split('/')
table_info = list(map(int, inp[0].split()))
table_size = table_info[0]
max_collision = table_info[1]
threshold = table_info[2]
data = list(map(int, inp[1].split()))

hash_table = HashTable(table_size, max_collision, threshold)
print("Initial Table :")
hash_table.print_table()

for key in data:
    hash_table.add_data(key)
