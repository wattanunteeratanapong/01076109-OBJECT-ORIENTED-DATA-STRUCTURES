# Chapter : 9 - item : 4 - Sort by alphabet

# ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่ในแต่ละ string โดยตัวอักษรจะมีแค่ a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น
# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

# Test Case 1
# Enter Input : 932c 832u32 2344b
# 2344b 932c 832u32

# Test Case 2
# Enter Input : 99a 78b c2345 11d
# 99a 78b c2345 11d

# Test Case 3
# Enter Input : 572z 5y5 304q2
# 304q2 5y5 572z

def sort_by_alphabet(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if get_alpha(arr[j]) > get_alpha(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def get_alpha(s):
    for char in s:
        if 'a' <= char <= 'z':  
            return char
    return ''

input_data = input("Enter Input : ").split()

sorted_data = sort_by_alphabet(input_data)
print(" ".join(sorted_data))
