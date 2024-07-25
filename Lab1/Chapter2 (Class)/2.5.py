# Chapter : 2 - item : 5 - รหัสลับ

# ตึกลึกลับแห่งหนึ่งเมื่อเดินไปข้างหลังจะมีคนบอกรหัสลับมาจงสร้างฟังชั่นคำนวณรหัส
# โดยรหัสจะประกอบไปด้วย english word that have repeat character
# เช่น bon("ball") = 48 หรือ bon("aah") = 4

def bon(secret_code):
    for i in range(len(secret_code)):
        if secret_code[i] in secret_code[i+1:]:
            repeat_char = secret_code[i]
            break
    
    alphabet_position = ord(repeat_char.lower()) - ord('a') + 1
    
    result = alphabet_position * 4
    
    return result


secret_code = input("Enter secret code : ")
print(bon(secret_code))