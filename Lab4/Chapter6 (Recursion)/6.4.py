# Chapter : 6 - item : 4 - Perket

# “เปอร์เกต์” เป็นอาหารแสนอร่อยที่ใครๆก็รู้จักกัน และแน่นอนว่าส่วนผสมย่อมเป็นสิ่งที่ต้องพิถีพิถันอย่างยิ่ง
# คุณมีส่วนผสมทั้งหมด N ชนิด แต่ละชนิดจะมีความเปรี้ยว S และความขม B เมื่อนำส่วนผสมมารวมกัน ความเปรี้ยว ลัพธ์ จะได้จากผลคูณของค่าความเปรี้ยวของทุกชนิดที่ใช้ ในขณะที่ความขมลัพธ์ จะได้จากผลบวกของความขมของ ทุกชนิดที่ใช้ ส่วนผสมที่ใช้นั้น
# เปอร์เกต์ที่อร่อยที่สุดนั้น จะมีผลต่างค่าความเปรี้ยวลัพธ์และค่าความขมลัพธ์ของส่วนผสมทั้งหมดน้อยที่สุด และเรา จำเป็นต้องใช้ส่วนผสมอย่างน้อย 1 ชนิด
# โจทย์ จงเขียนโปรแกรมเพื่อหาค่าผลต่างของความเปรี้ยวลัพธ์และความขมลัพธ์ของส่วนผสม ที่น้อยที่สุด
# ******* อธิบาย input
# โดยส่วนผสมแต่ละชนิดจะแบ่งด้วย comma ( ' , ' ) โดยในแต่ละส่วนผสม จะมีจำนวนเต็มสองจำนวน S และ B คือค่าความเปรี้ยวและค่าความขมของ ส่วนผสมชนิดนั้น
# ******* รับประกันว่าสำหรับทุกข้อมูลนำเข้า เมื่อนำส่วนผสมทุกชนิดแล้ว จะได้ค่าความเปรี้ยวลัพธ์และความขมลัพธ์ ไม่เกิน 1,000,000,000

# Test Case 1
# Enter Input : 3 10
# 7

# Test Case 2
# Enter Input : 3 8,5 8
# 1

# Test Case 3
# Enter Input : 1 7,2 6,3 8,4 9
# 1

def min_diff(ingredients, idx=0, sour=1, bitter=0, used=False):
    if idx == len(ingredients):
        if not used:  
            return float('inf')
        return abs(sour - bitter)
    exclude = min_diff(ingredients, idx + 1, sour, bitter, used)
    include = min_diff(ingredients, idx + 1, sour * ingredients[idx][0], bitter + ingredients[idx][1], True)
    return min(exclude, include)

input_data = input("Enter Input : ")
ingredients = [tuple(map(int, x.split())) for x in input_data.split(",")]
result = min_diff(ingredients)
print(result)