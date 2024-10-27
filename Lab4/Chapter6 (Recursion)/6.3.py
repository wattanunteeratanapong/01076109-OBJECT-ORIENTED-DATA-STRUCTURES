# Chapter : 6 - item : 3 - ( 2^(input) ) - 1

# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
# เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง  หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! ! 
# *** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11

# Test Case 1
# Enter Number : -1
# Only Positive & Zero Number ! ! !

# Test Case 2
# Enter Number : 0
# 0

# Test Case 3
# Enter Number : 1
# 0
# 1

# Test Case 4
# Enter Number : 4
# 0000
# 0001
# 0010
# 0011
# 0100
# 0101
# 0110
# 0111
# 1000
# 1001
# 1010
# 1011
# 1100
# 1101
# 1110
# 1111

def generate_binaries(n):
    if n < 0:
        return ["Only Positive & Zero Number ! ! !"]
    if n == 0:
        return ["0"]
    
    def int_to_binary(x, length):
        return bin(x)[2:].zfill(length)
    
    result = []
    max_number = 2 ** n
    for i in range(max_number):
        result.append(int_to_binary(i, n))
    
    return result

n = int(input("Enter Number : "))
results = generate_binaries(n)
for result in results:
    print(result)