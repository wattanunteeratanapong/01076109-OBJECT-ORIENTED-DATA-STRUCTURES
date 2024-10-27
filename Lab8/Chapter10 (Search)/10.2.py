# Chapter : 10 - item : 2 - First Greater Value

# ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000
# ***** อธิบาย Test Case 2:
# Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
# 1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
# 2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
# 3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value

# Test Case 1
# Enter Input : 3 2 7 6 8/5
# 6

# Test Case 2
# Enter Input : 3 2 7 6 8/5 6 12
# 6
# 7
# No First Greater Value

def first_greater_value(arr, targets):
    arr.sort()  
    
    def binary_search(arr, target):
        l, r = 0, len(arr) - 1
        result = -1  
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > target:
                result = arr[mid]  
                r = mid - 1  
            else:
                l = mid + 1 
        return result
    
    result = []
    for target in targets:
        greater_value = binary_search(arr, target)
        if greater_value != -1:
            result.append(str(greater_value))
        else:
            result.append("No First Greater Value")
    
    return '\n'.join(result)

inp = input('Enter Input : ').split('/')
arr = list(map(int, inp[0].split()))  
targets = list(map(int, inp[1].split())) 

print(first_greater_value(arr, targets))
