# Chapter : 9 - item : 3 - somethingDROME

# รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้
# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"
# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"
# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"
# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"
# - หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"
# - หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"
# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

# Test Case 1
# Enter Input : 1357
# Metadrome

# Test Case 2
# Enter Input : 12344
# Plaindrome

# Test Case 3
# Enter Input : 7531
# Katadrome

# Test Case 4
# Enter Input : 9874441
# Nialpdrome

# Test Case 5
# Enter Input : 666
# Repdrome

# Test Case 6
# Enter Input : 1985
# Nondrome

def sort_asc(num_list):
    for i in range(len(num_list)):
        for j in range(0, len(num_list)-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list

def sort_desc(num_list):
    for i in range(len(num_list)):
        for j in range(0, len(num_list)-i-1):
            if num_list[j] < num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list

def check_drome(number):
    num_list = [int(x) for x in number]
    
    if len(set(num_list)) == 1:
        return "Repdrome"

    asc_sorted = sort_asc(num_list[:])  
    desc_sorted = sort_desc(num_list[:])  
    
    if num_list == asc_sorted:
        if len(num_list) == len(set(num_list)):
            return "Metadrome"
        else:
            return "Plaindrome"
    
    if num_list == desc_sorted:
        if len(num_list) == len(set(num_list)):
            return "Katadrome"
        else:
            return "Nialpdrome"
    
    return "Nondrome"

number = input("Enter Input : ")

print(check_drome(number))

