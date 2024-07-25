# Chapter : 1 - item : 1 - รับ h m s --> คำนวณวินาที

# รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
# เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที
# แล้วแสดงผลเป็น วินาที
# แสดงผลตามตัวอย่าง

print("*** Converting hh.mm.ss to seconds ***")
hh, mm, ss = map(int, input("Enter hh mm ss : ").split())

if(mm>59):
    print(f"mm({mm}) is invalid!")
elif(ss>59):
    print(f"ss({ss}) is invalid!")
elif(mm<0):
    print(f"mm({mm}) is invalid!")
elif(ss<0):
    print(f"ss({ss}) is invalid!")
else:
    real_hour = hh * 60 * 60
    real_minute = mm * 60

    second = real_hour + real_minute + ss
    string_second = str(second)


print(f"{hh:02}:{mm:02}:{ss:02} = {second:,d} seconds")  

# Time Complexity
# O(1)

# Space Complexity
# O(1)