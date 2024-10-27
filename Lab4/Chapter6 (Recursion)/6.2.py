# Chapter : 6 - item : 2 - Length of a String EXTRA

# ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)
# ****ห้ามใช้คำสั่ง len, for, while, do while, split*****
# หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

# Test Case 1
# Enter Input : hello
# h*e~l*l~o*
# 5

# Test Case 2
# Enter Input : data structure is easy
# d*a~t*a~ *s~t*r~u*c~t*u~r*e~ *i~s* ~e*a~s*y~
# 22

# Test Case 3
# Enter Input : *~*~*~
# **~~**~~**~~
# 6

def length(txt):
    if txt == "":
        return 0
    else:
        return 1 + length(txt[1:])

def format_string(txt, index=0):
    if txt == "":
        return ""
    else:
        special_char = "*" if index % 2 == 0 else "~"
        return txt[0] + special_char + format_string(txt[1:], index + 1)

input_text = input("Enter Input : ")
formatted_text = format_string(input_text)

print(formatted_text)
print(length(input_text))
