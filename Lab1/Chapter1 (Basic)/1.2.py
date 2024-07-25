# Chapter : 1 - item : 2 - BMI Calculate

# รับ input 2 จำนวนโดยที่ input ที่ 1 คือ h เป็นค่าความสูง(เมตร) และ Input ที่ 2 คือ w เป็นค่าน้ำหนัก(กิโลกรัม) โดยให้คำนวณหาค่า BMI ที่คำนวณจากสูตร BMI = w / (h^2) โดยให้แสดงผลตามข้อความข้างล่าง
# BMI < 18.50 แสดงผล Less Weight
#18.50 <= BMI  < 23 แสดงผล Normal Weight
# 23 <= BMI  < 25 แสดงผล Morethan Normal Weight
# 25 <= BMI  < 30 แสดงผล Getting Fat
# BMI  >= 30 แสดงผล Fat

h, w = map(float, input("Enter your High and Weight : ").split())

BMI = w / (h**2)

if(BMI<18.5):
    print("Less Weight")
if(18.5<BMI<23):
    print("Normal Weight")
if(23<BMI<25):
    print("More than Normal Weight")
if(25<BMI<30):
    print("Getting Fat")
if(30<BMI):
    print("Fat") 

# Time Complexity
# O(1)

# Space Complexity
# O(1)