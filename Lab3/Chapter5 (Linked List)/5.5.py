# Chapter : 5 - item : 5 - Scramble

# เขียนโปรแกรมคลุกคำ (scramble) สร้าง singly linked list ของคำในจดหมาย scramble จดหมายโดยทำคล้ายตัด ไพ่และกรีดไพ่ ผู้รับจดหมาย descramble กรีดกลับและตัดกลับจนได้จดหมายฉบับเดิมที่อ่านได้(หากออกแบบดีๆ สามารถ scramble กี่ครั้งก็ได้ ขึ้นแรกให้ทำ ครั้งเดียวก่อน)  
# ***** รูปแบบ input *****
# แบ่งเป็น 2 ฝั่ง ได้แก่ ฝั่งซ้าย (Linked List เริ่มต้น  ความยาวขั้นต่ำของ Linked List รับประกันว่าขั้นต่ำคือ 10)  |  ฝั่งขวา BottomUp กับ Riffle โดยการแทนด้วย B กับ R ซึ่งการรับ R กับ B สามารถสลับที่กันได้ เช่น   R 40,B 60  <->  B 60,R 40
# 1.  B   < percentage >  :  bottomUp ตัด ยกส่วนบน (lift) ออกตาม % input ที่รับเข้ามา นำส่วนล่างมาซ้อนทับส่วนบน
# 2.  R   < percentage >  :  riffleShuffle กรีด (จากด้านบน) lift ตาม % นำ node ของแต่ละลิสต์มาสลับกันทีละ node จากต้นลิสต์ ส่วนเกินนำมาต่อท้าย
# ***** ถ้าหากคิดเปอร์เซ็นของความยาว Linked List แล้วได้ทศนิยม ให้ปัดลงทั้งหมด *****
# ***** การแสดงผลมี Pattern เป็น   Bottomup  ->  Riffle  ->  Deriffle  -> Debottomup นะครับ

# Test Case 1
# Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 62,B 23
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3
# Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
# Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
# Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 50.000 % : 6 7 8 9 10 1 2 3 4 5
# Riffle 50.000 % : 6 1 7 2 8 3 9 4 10 5
# Deriffle 50.000 % : 6 7 8 9 10 1 2 3 4 5
# Debottomup 50.000 % : 1 2 3 4 5 6 7 8 9 10
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 23.000 % : 3 4 5 6 7 8 9 10 1 2
# Riffle 62.000 % : 3 9 4 10 5 1 6 2 7 8
# Deriffle 62.000 % : 3 4 5 6 7 8 9 10 1 2
# Debottomup 23.000 % : 1 2 3 4 5 6 7 8 9 10
# --------------------------------------------------

# Test Case 2
# Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 16.98,B 68.42|R 26.9257,B 57
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3
# Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
# Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
# Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 50.000 % : 6 7 8 9 10 1 2 3 4 5
# Riffle 50.000 % : 6 1 7 2 8 3 9 4 10 5
# Deriffle 50.000 % : 6 7 8 9 10 1 2 3 4 5
# Debottomup 50.000 % : 1 2 3 4 5 6 7 8 9 10
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 68.420 % : 7 8 9 10 1 2 3 4 5 6
# Riffle 16.980 % : 7 8 9 10 1 2 3 4 5 6
# Deriffle 16.980 % : 7 8 9 10 1 2 3 4 5 6
# Debottomup 68.420 % : 1 2 3 4 5 6 7 8 9 10
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 57.000 % : 6 7 8 9 10 1 2 3 4 5
# Riffle 26.926 % : 6 8 7 9 10 1 2 3 4 5
# Deriffle 26.926 % : 6 7 8 9 10 1 2 3 4 5
# Debottomup 57.000 % : 1 2 3 4 5 6 7 8 9 10
# --------------------------------------------------

# Test Case 3
# Enter Input : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20/B 32.4367,R 49.5484863|B 89.4642,R 12.8962|R 11.546678,B 20.77867|R 40.56,B 93.7567
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# BottomUp 32.437 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4 5 6
# Riffle 49.548 % : 7 16 8 17 9 18 10 19 11 20 12 1 13 2 14 3 15 4 5 6
# Deriffle 49.548 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4 5 6
# Debottomup 32.437 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# BottomUp 89.464 % : 18 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# Riffle 12.896 % : 18 20 19 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# Deriffle 12.896 % : 18 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# Debottomup 89.464 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# BottomUp 20.779 % : 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
# Riffle 11.547 % : 5 7 6 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
# Deriffle 11.547 % : 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
# Debottomup 20.779 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# BottomUp 93.757 % : 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
# Riffle 40.560 % : 19 7 20 8 1 9 2 10 3 11 4 12 5 13 6 14 15 16 17 18
# Deriffle 40.560 % : 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
# Debottomup 93.757 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# --------------------------------------------------

# Test Case 4
# Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 10,B 20|B 27,R 73
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3
# Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
# Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
# Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 50.000 % : 6 7 8 9 10 1 2 3 4 5
# Riffle 50.000 % : 6 1 7 2 8 3 9 4 10 5
# Deriffle 50.000 % : 6 7 8 9 10 1 2 3 4 5
# Debottomup 50.000 % : 1 2 3 4 5 6 7 8 9 10
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 20.000 % : 3 4 5 6 7 8 9 10 1 2
# Riffle 10.000 % : 3 4 5 6 7 8 9 10 1 2
# Deriffle 10.000 % : 3 4 5 6 7 8 9 10 1 2
# Debottomup 20.000 % : 1 2 3 4 5 6 7 8 9 10
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10
# BottomUp 27.000 % : 3 4 5 6 7 8 9 10 1 2
# Riffle 73.000 % : 3 10 4 1 5 2 6 7 8 9
# Deriffle 73.000 % : 3 4 5 6 7 8 9 10 1 2
# Debottomup 27.000 % : 1 2 3 4 5 6 7 8 9 10
# --------------------------------------------------

# Test Case 5
# Enter Input : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30/B 89.4642,R 12.8962|R 11.546678,B 20.77867|R 40.56,B 93.7567|B 27.5495,R 73.1597
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# BottomUp 89.464 % : 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
# Riffle 12.896 % : 27 30 28 1 29 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
# Deriffle 12.896 % : 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
# Debottomup 89.464 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# BottomUp 20.779 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6
# Riffle 11.547 % : 7 10 8 11 9 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6
# Deriffle 11.547 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6
# Debottomup 20.779 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# BottomUp 93.757 % : 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
# Riffle 40.560 % : 29 11 30 12 1 13 2 14 3 15 4 16 5 17 6 18 7 19 8 20 9 21 10 22 23 24 25 26 27 28
# Deriffle 40.560 % : 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
# Debottomup 93.757 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# BottomUp 27.549 % : 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8
# Riffle 73.160 % : 9 30 10 1 11 2 12 3 13 4 14 5 15 6 16 7 17 8 18 19 20 21 22 23 24 25 26 27 28 29
# Deriffle 73.160 % : 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8
# Debottomup 27.549 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# --------------------------------------------------

# Test Case 6
# Enter Input : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30/B 12.4642,R 89.8962|R 20.546678,B 11.77867|R 34.56,B 93.7567|B 79.5495,R 97.1597
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# BottomUp 12.464 % : 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3
# Riffle 89.896 % : 4 30 5 1 6 2 7 3 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
# Deriffle 89.896 % : 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3
# Debottomup 12.464 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# BottomUp 11.779 % : 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3
# Riffle 20.547 % : 4 10 5 11 6 12 7 13 8 14 9 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3
# Deriffle 20.547 % : 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3
# Debottomup 11.779 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# BottomUp 93.757 % : 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
# Riffle 34.560 % : 29 9 30 10 1 11 2 12 3 13 4 14 5 15 6 16 7 17 8 18 19 20 21 22 23 24 25 26 27 28
# Deriffle 34.560 % : 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
# Debottomup 93.757 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# BottomUp 79.549 % : 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# Riffle 97.160 % : 24 23 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
# Deriffle 97.160 % : 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# Debottomup 79.549 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# --------------------------------------------------

# Test Case 7
# Enter Input : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30/B 64.2354,R 5.13542|R 98.4121,B 4.21952|R 12.345,B 67.89
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# BottomUp 64.235 % : 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# Riffle 5.135 % : 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# Deriffle 5.135 % : 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# Debottomup 64.235 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# BottomUp 4.220 % : 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1
# Riffle 98.412 % : 2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# Deriffle 98.412 % : 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1
# Debottomup 4.220 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# --------------------------------------------------
# Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# BottomUp 67.890 % : 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# Riffle 12.345 % : 21 24 22 25 23 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# Deriffle 12.345 % : 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# Debottomup 67.890 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# --------------------------------------------------

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)


class LinkedList:
  def __init__(self):
    self.head = None

  def __str__(self):
    if self.isEmpty():
      return "Empty"
    cur, s = self.head, str(self.head.value) + " "
    while cur.next != None:
      s += str(cur.next.value) + " "
      cur = cur.next
    return s

  def isEmpty(self):
    return self.head == None

  def append(self, item):
    new_node = Node(item)
    if self.head == None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next != None:
        cur = cur.next
      cur.next = new_node

  def addHead(self, item):
    new_node = Node(item)
    new_node.next = self.head
    self.head = new_node

  def search(self, item):
    cur = self.head
    while cur != None:
      if cur.value == item:
        return cur
      cur = cur.next
    return None

  def index(self, item):
    cur = self.head
    idx = 0
    while cur != None:
      if cur.value == item:
        return idx
      cur = cur.next
      idx += 1
    return -1

  def size(self):
    size = 0
    cur = self.head
    while cur != None:
      cur = cur.next
      size += 1
    return size

  def pop(self, pos):
    if self.isEmpty() or pos < 0 or pos >= self.size():
      return "Out of Range"

    if pos == 0:
      removed_value = self.head.value
      self.head = self.head.next
    else:
      prev = None
      cur = self.head
      count = 0
      while cur != None and count < pos:
        prev = cur
        cur = cur.next
        count += 1
      removed_value = cur.value
      prev.next = cur.next

    return "Success"

  def bottom_up(self, pos, size):
    if self.isEmpty() or pos < 0 or pos >= self.size():
      return None
    else:
      cur = self.head
      count = 0
      while cur is not None and count < pos - 1:
        cur = cur.next
        count += 1

      new_head = cur.next
      cur.next = None

      cur = new_head
      while cur.next is not None:
        cur = cur.next

      cur.next = self.head
      self.head = new_head

  def de_bottom_up(self, pos, size):
    if self.isEmpty() or pos < 0 or pos >= self.size():
      return None
    else:
      cur = self.head
      count = 0
      while cur is not None and count < pos - 1:
        cur = cur.next
        count += 1

      new_head = cur.next
      cur.next = None

      cur = new_head
      while cur.next is not None:
        cur = cur.next

      cur.next = self.head
      self.head = new_head

  def riffle(self, pos, size):
    if self.isEmpty() or pos < 0 or pos >= self.size():
      return None

    else:
      list1 = LinkedList()
      list2 = LinkedList()

      cur = self.head
      count = 0
      while cur is not None and count < pos - 1:
        cur = cur.next
        count += 1

      list2.head = cur.next
      cur.next = None

      list1.head = self.head
      self.head = None

      cur1 = list1.head
      cur2 = list2.head

      while cur1 is not None and cur2 is not None:
        self.append(cur1.value)
        self.append(cur2.value)
        cur1 = cur1.next
        cur2 = cur2.next

      while cur1 is not None:
        self.append(cur1.value)
        cur1 = cur1.next

      while cur2 is not None:
        self.append(cur2.value)
        cur2 = cur2.next

  def de_riffle(self, pos, size):
    if self.isEmpty() or pos < 0 or pos >= self.size():
      return None

    else:
      if pos < size / 2:
        pull_out = pos - 1
      elif pos >= size / 2:
        pull_out = size - pos

      list1 = LinkedList()
      cur = self.head
      while cur is not None:
        if cur.next is not None and list1.size() < pull_out:
          list1.append(cur.next)
          cur.next = cur.next.next
        cur = cur.next

      if list1.isEmpty():
        return None

      cur = list1.head
      while cur.next is not None:
        cur = cur.next
      cur.next = None

      if pos < size / 2:
        cur = self.head
        count = 0
        while cur is not None and count < pos - 1:
          cur = cur.next
          count += 1

        search_cur = cur

        cur = list1.head
        while cur.next is not None:
          cur = cur.next

        cur.next = search_cur.next
        search_cur.next = list1.head
      elif pos >= size / 2:
        cur = self.head
        while cur.next is not None:
          cur = cur.next
        cur.next = list1.head


def createLL(LL):
  linked_list = LinkedList()
  for l in LL:
    linked_list.append(l)
  return linked_list


def printLL(head):
  return head


def SIZE(head):
  return head.size()


def scarmble(head, b, r, size):
  pos_b, pos_r = int(b / 100 * size), int(r / 100 * size)
  head.bottom_up(pos_b, size)
  print(f"BottomUp {b:.3f} % : {head}")
  head.riffle(pos_r, size)
  print(f"Riffle {r:.3f} % : {head}")
  head.de_riffle(pos_r, size)
  print(f"Deriffle {r:.3f} % : {head}")
  head.de_bottom_up(size - pos_b, size)
  print(f"Debottomup {b:.3f} % : {head}")


inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
  print("Start : {0}".format(printLL(h)))
  k = i.split(',')
  if k[0][0] == "B" and k[1][0] == "R":
    scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
  elif k[0][0] == "R" and k[1][0] == "B":
    scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
  print('-' * 50)