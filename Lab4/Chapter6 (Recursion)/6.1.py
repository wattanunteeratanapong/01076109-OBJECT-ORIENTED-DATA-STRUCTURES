# Chapter : 6 - item : 1 - หาค่าน้อยที่สุด

# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
# ให้เขียน Recursive หาค่า Min ของ Input

# Test Case 1
# Enter Input : 8 7 10 1 5 4 2 6 3 9
# Min : 1

# Test Case 2
# Enter Input : -84 -230 -54845 -6 -1
# Min : -54845

nums = input("Enter Input : ").split()

def find_min(nums):
    if len(nums) == 1:
        return int(nums[0])
    else:
        return min(int(nums[0]), find_min(nums[1:]))
    
print("Min : " + str(find_min(nums)))