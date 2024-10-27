# Chapter : 9 - item : 1 - bubble sort [recursive]

# เขียน function bubble sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive
# ***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***
# *** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

# Test Case 1
# Enter Input : 4 3 2 1
# [1, 2, 3, 4]

# Test Case 2
# Enter Input : 3 2 1 5 6 7
# [1, 2, 3, 5, 6, 7]

# Test Case 3
# Enter Input : 1 2 3 4 5
# [1, 2, 3, 4, 5]

def bubble_sort_recursive(lst, n=None):
    if n is None:
        n = len(lst)
    
    if n == 1:
        return lst
    
    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    
    return bubble_sort_recursive(lst, n - 1)

input_str = input("Enter Input : ")
lst = list(map(int, input_str.split()))

sorted_lst = bubble_sort_recursive(lst)
print(sorted_lst)
