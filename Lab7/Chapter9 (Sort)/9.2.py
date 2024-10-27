# Chapter : 9 - item : 2 - เรียงลำดับโดยไม่สนจำนวนเต็มลบ

# ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน
# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

# Test Case 1
# Enter Input : 6 3 -2 5 -8 2 -2
# 2 3 -2 5 -8 6 -2

# Test Case 2
# Enter Input : 6 5 4 -1 3 0 2 -99 1
# 0 1 2 -1 3 4 5 -99 6

def sort_non_negative_elements(arr):
    pos_values = [val for val in arr if val >= 0]
    
    for idx in range(len(pos_values)):
        for nxt in range(idx + 1, len(pos_values)):
            if pos_values[idx] > pos_values[nxt]:
                pos_values[idx], pos_values[nxt] = pos_values[nxt], pos_values[idx]

    pos_val_idx = 0
    for idx in range(len(arr)):
        if arr[idx] >= 0:
            arr[idx] = pos_values[pos_val_idx]
            pos_val_idx += 1

    return arr


input_values = input("Enter Input : ").split()
arr = list(map(int, input_values))

sorted_result = sort_non_negative_elements(arr)
print(" ".join(map(str, sorted_result)))
