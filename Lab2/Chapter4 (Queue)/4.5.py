# Chapter : 4 - item : 5 - Color Crush 2

# เกม Color Crush คืออะไร : Color Crush จะเป็นเกมที่นำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  ABBBA  -> AA  เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  ถ้าหากมีการเรียงกันแบบ  ABBBAA -> Empty  เนื่องจาก  ถ้าหาก B ระเบิด  A(BBB)AA -> AAA จะเห็นว่า A ก็เรียงกันอีก 3 ตัวทำให้เกิดการระเบิดขึ้นอีกครั้งหนึ่ง  และถ้าหากมีการเรียงกันแบบ AAAA -> A เนื่องจากมีการเรียงกัน 3 ตัว  (AAA)A ทำให้เหลือ A 1 ตัว
# เนื้อเรื่อง :  หลังจากที่กฤษฎาได้เล่นเกม Color Crush ก็ได้ไปเห็นโฆษณาว่า บริษัทที่ได้สร้าง Color Crush มีแผนการที่จะสร้างเกม Color Crush 2 ขึ้นมา กฤษฎาจึงได้สมัครเข้าไปร่วมทีมในการสร้างเกม Color Crush 2 ซึ่งเกมนี้จะมีกิมมิคที่แตกต่างออกไป คือการที่จะมี 2 ฝั่ง คือ ฝั่งปกติกับฝั่งโลกกระจก โดยฝั่งโลกกระจกจะเกิดการระเบิดก่อน ซึ่งการระเบิดของฝั่งโลกกระจกจะไม่ใช่ระเบิดแล้วหายไปเลย แต่จะเป็นระเบิดแล้วกลายเป็น ITEM ไว้สำหรับขัดขวางการระเบิดของฝั่งปกติ  หลังจากที่ฝั่งโลกกระจกเกิดการระเบิดครบแล้ว ก็จะเป็นคิวของฝั่งปกติ  ซึ่งถ้าหากฝั่งปกติมีการเรียงกันของสีที่จะทำให้เกิดการระเบิด ในเสี้ยววินาทีนั้นก่อนที่จะเกิดการระเบิดของฝั่งปกติ  ITEM สำหรับขัดขวางการระเบิดของฝั่งโลกกระจก จะมาคั่นระหว่างระเบิดลูกที่ 2 กับ ลูกที่ 3 (อาจจะทำให้เกิดการระเบิดเหมือนเดิมได้ถ้าหาก ระเบิดนั้นเป็นสีเดียวกัน  แต่ถ้าเป็นคนละสีก็จะทำให้ไม่เกิดการระเบิดขึ้น)  โดยระเบิดอาจจะเกิดการระเบิดซ้อนๆกันเรื่อยๆได้จะเป็น Empty  เช่น ถ้าหากฝั่งปกติมีระเบิดเรียงแบบนี้ AAAAA และฝั่งโลกกระจกมีระเบิดแบบนี้ AAA ถ้าหากฝั่งปกติระเบิดธรรมดา 1 ทีจะเหลือแค่ AA แต่ถ้าหากฝั่งโลกกระจกมาขัดขวาง จะกลายเป็น AA(A)AAAA ก็จะเกิดระเบิด 2 ทีทำให้ระเบิดฝั่งปกติเป็น Empty
# อธิบายรูปแบบ Input ของ Test_Case_1 : ฝั่งปกติจะมีระเบิดเรียงดังนี้ -> AAABBBCDEE  ฝั่งโลกกระจกจะมีระเบิดเรียงดังนี้ -> HHH โดยฝั่งโลกกระจกจะมีระเบิด H ที่เป็น ITEM สำหรับขัดขวาง 1 ลูกไว้สำหรับขัดขวางการระเบิดที่จะเกิดขึ้นกับฝั่งปกติได้  ต่อมาฝั่งปกติจะเกิดการระเบิดของ A และ B ตามลำดับ  โดยฝั่งโลกกระจกจะนำระเบิด H ไปขัดขวางการระเบิดของระเบิด A เพราะระเบิด A เกิดการระเบิดก่อนระเบิด B  โดยการขัดระเบิดนั้นจะเป็นการขัดระหว่างลูกที่ 2 กับลูกที่ 3 เพื่อให้เห็นภาพ -> AAABBBCDEE -> AA(H)ABBBCDEE  -> AA(H)ACDEE ลำดับจะเป็นดังนี้  และฝั่งปกติเกิดการระเบิด 1 ครั้ง ส่วนฝั่งโลกกระจกก็เกิดการระเบิดอีก 1 ครั้ง
# อธิบายรูปแบบ Input ของ Test_Case_3 : ฝั่งปกติจะมีระเบิดเรียงดังนี้ -> AAABBBCDDDEE  ฝั่งโลกกระจกจะมีระเบิดเรียงดังนี้ -> BBBTENETAAA โดยฝั่งโลกกระจกจะมีระเบิด A และ B ที่เป็น ITEM สำหรับขัดขวาง 2 ลูกตามลำดับไว้สำหรับป้องกันการระเบิดที่จะเกิดขึ้นกับฝั่งปกติได้  ต่อมาฝั่งปกติจะเกิดการระเบิดของ A B และ D ตามลำดับ  โดยฝั่งโลกกระจกจะนำระเบิด A  ไปขัดขวางการระเบิดของระเบิด A เพราะระเบิด A เกิดการระเบิดก่อนระเบิด B  โดยการขัดระเบิดนั้นจะเป็นการขัดระหว่างลูกที่ 2 กับลูกที่ 3  เพื่อให้เห็นภาพ -> AAABBBCDDDEE -> AA(A)ABBBCDDDEE -> ABBBCDDDEE ลำดับจะเป็นดังนี้  ต่อมาจะนำระเบิด B ไปขัดขวางการระเบิดของระเบิด B เพื่อให้เห็นภาพ  ABBBCDDDEE -> ABB(B)BCDDDEE -> ABCDDDEE  ต่อมาเกิดการระเบิดอีก 1 ครั้ง ABCDDDEE -> ABCEE ซึ่งฝั่งโลกกระจกไม่สามารถขัดขวางได้เพราะ ITEM สำหรับขัดขวางหมดแล้ว   และฝั่งปกติเกิดการระเบิดทั้งหมด 3 ครั้ง  ซึ่ง 2 ครั้งเกิดจากการที่ฝั่งโลกกระจกใส่ระเบิดสีเดียวกันมาซึ่งถือว่าเป็นการขัดขวางที่ผิดหและเกิดการระเบิดเองอีก 1 ครั้ง ส่วนฝั่งโลกกระจกก็เกิดการระเบิดอีก 2 ครั้ง
# อธิบายรูปแบบ Output : แบ่งออกเป็น 2 ฝั่งคือฝั่งปกติกับฝั่งโลกกระจก  โดยบรรทัดแรกจะเป็นจำนวนระเบิดที่เหลืออยู่ บรรทัดที่สองจะเป็นระเบิดที่เหลืออยู่แต่ถ้าหากไม่มีระเบิดเหลืออยุ่เลยให้แสดง "Empty" บรรทัดที่สามจะเป็นจำนวนที่เกิดระเบิดขึ้น บรรทัดที่สี่จะมีเฉพาะฝั่งปกติถ้าหากเกิดเหตุการณ์ที่ ITEM ของฝั่งโลกกระจกมาขัดขวาง แต่ระเบิดนั้นดันเป็นลูกเดียวกับที่จะเกิดการระเบิด  ส่วนทีมสีน้ำเงินจะเหมือนกับทีมสีแดงแต่บรรทัดที่ 2 กับ 3 และชื่อทีม จะเป็นแบบ inverse
# คำใบ้ - ใช้ Stack ในการหาลูกระเบิดเรียงกัน 3 ลูก   โดยให้ทำฝั่งโลกกระจกก่อนว่ามีระเบิดลูกอะไรบ้าง (ก่อนเข้า stack ให้ Reverse ก่อน)  จากนั้นเก็บลง Queue แล้วไปทำฝั่งปกติถ้าหากฝั่งปกติเกิดการระเบิดก็ DeQueue ระเบิดที่ได้รับมาจากฝั่งกระจกมาขัดระเบิดระหว่างลูกที่ 2 กับ 3
# อธิบาย Case 10:
# ฝั่งซ้าย = DDDFFFGGG
# ฝั่งขวา = ABBBAACCC
# ทำฝั่งขวาก่อนโดยการ inverse ABBBAACCC -> CCCAABBBA จะได้ระเบิดมา 3 ลูกคือ C B A ตามลำดับจากนั้นเก็บลง Queue ต่อมาดูที่ฝั่งซ้าย DDD จะเกิดการระเบิดเราจะนำ C ไปขัด | ต่อมา F จะระเบิดเราจะนำ B มาขัด | ต่อมา G จะระเบิดเราจะนำ A มาขัด   สุดท้ายจะกลายเป็น DDCDFFBFGGAG

# Test Case 1
# Enter Input (Normal, Mirror) : AAABBBCDEE HHH
# NORMAL :
# 8
# EEDCAHAA
# 1 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 0
# ytpmE
# (RORRIM) ! ! ! (s)evisolpxE 1

# Test Case 2
# Enter Input (Normal, Mirror) : AAABBBCDEE FGHHHIOPPP
# NORMAL :
# 12
# EEDCBHBBAPAA
# 0 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 4
# FGIO
# (RORRIM) ! ! ! (s)evisolpxE 2

# Test Case 3
# Enter Input (Normal, Mirror) : AAABBBCDDDEE BBBTENETAAA
# NORMAL :
# 5
# EECBA
# 1 Explosive(s) ! ! ! (NORMAL)
# Failed Interrupted 2 Bomb(s)
# ------------MIRROR------------
# : RORRIM
# 5
# TENET
# (RORRIM) ! ! ! (s)evisolpxE 2

# Test Case 4
# Enter Input (Normal, Mirror) : AAABBBDDD TENET
# NORMAL :
# 0
# Empty
# 3 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 5
# TENET
# (RORRIM) ! ! ! (s)evisolpxE 0

# Test Case 5
# Enter Input (Normal, Mirror) : AAABBBCDDDEE OOOZZZTENETXXXYYY
# NORMAL :
# 15
# EEDZDDCBXBBAYAA
# 0 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 5
# TENET
# (RORRIM) ! ! ! (s)evisolpxE 4

# Test Case 6
# Enter Input (Normal, Mirror) : DDDFFFGGG ABBBAACCC
# NORMAL :
# 12
# GAGGFBFFDCDD
# 0 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 0
# ytpmE
# (RORRIM) ! ! ! (s)evisolpxE 3

# Test Case 7
# Enter Input (Normal, Mirror) : AJJJJJJJAA JJJJJJ
# NORMAL :
# 0
# Empty
# 2 Explosive(s) ! ! ! (NORMAL)
# Failed Interrupted 2 Bomb(s)
# ------------MIRROR------------
# : RORRIM
# 0
# ytpmE
# (RORRIM) ! ! ! (s)evisolpxE 2

# Test Case 8
# Enter Input (Normal, Mirror) : PPPAAAABBBB PPPAAAA
# NORMAL :
# 10
# BAAPAAPAPP
# 1 Explosive(s) ! ! ! (NORMAL)
# ------------MIRROR------------
# : RORRIM
# 1
# A
# (RORRIM) ! ! ! (s)evisolpxE 2

class CustomQueue:
    def __init__(self, elements=None):
        if elements is None:
            self.items = []
        else:
            self.items = elements

    def add(self, element):
        self.items.append(element)

    def remove(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def count(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def eliminate_duplicates(element, lst):
    for _ in range(2):
        lst.remove(element)
    return element


def process_mirror_elements(mirror_queue):
    processed = [mirror_queue.remove() for _ in range(mirror_queue.count())]
    remaining = ""
    duplicates_queue = CustomQueue()
    storage_queue = CustomQueue()
    duplicate_count = 0
    for item in processed:
        if processed.count(item) > 2:
            duplicates_queue.add(eliminate_duplicates(item, processed))
            storage_queue.add(item)
            duplicate_count += 1
        else:
            remaining += str(item)
    return duplicates_queue, storage_queue, remaining, duplicate_count


def resolve_disruptors(normal_queue, duplicate_queue):
    previous = ""
    penultimate = ""
    result_queue = CustomQueue()
    while not normal_queue.is_empty():
        current = normal_queue.remove()
        if duplicate_queue.is_empty():
            result_queue.add(current)
            continue
        if current == previous and previous != penultimate:
            penultimate = previous
        elif previous == current and current == penultimate:
            result_queue.add(duplicate_queue.remove())
        previous = current
        result_queue.add(current)
    return result_queue


def verify_mirror_bombs(sequence, storage_queue):
    count_first = 0
    count_second = 0
    failed_count = 0
    idx_first = 0
    idx_second = 0

    for _ in range(storage_queue.count()):
        char = storage_queue.remove()
        fail_sequence = str(char * 4)
        if fail_sequence in sequence:
            sequence = sequence.replace(fail_sequence, char, 1)
            failed_count += 1

    while idx_first < len(sequence):
        bomb = str(sequence[idx_first] * 3)
        if bomb in sequence[idx_first:]:
            sequence = sequence.replace(bomb, "", 1)
            count_first += 1
        idx_first += 1

    while idx_second < len(sequence):
        bomb = str(sequence[idx_second] * 3)
        if bomb in sequence[idx_second:]:
            sequence = sequence.replace(bomb, "", 1)
            count_second += 1
        idx_second += 1

    return sequence, count_first, count_second, failed_count


def process_input(input_string):
    parts = input_string.split(" ")
    normal_queue = CustomQueue([char for char in parts[0]])
    mirror_queue = CustomQueue([char for char in parts[1]])

    duplicates_queue, storage_queue, remaining_string, disrupt_count = process_mirror_elements(mirror_queue)
    interupted_sequence = resolve_disruptors(normal_queue, CustomQueue([duplicates_queue.remove() for _ in range(duplicates_queue.count())][::-1]))
    processing_sequence = str("".join([interupted_sequence.remove() for _ in range(interupted_sequence.count())][::-1]))
    final_sequence, count_first, count_second, failed_count = verify_mirror_bombs(processing_sequence, storage_queue)

    print(f"NORMAL :\n{len(final_sequence)}")
    string_first = final_sequence if len(final_sequence) != 0 else "Empty"
    print(string_first)
    print(f"{count_first + count_second} Explosive(s) ! ! ! (NORMAL)")
    if failed_count != 0:
        print(f"Failed Interrupted {failed_count} Bomb(s)")
    print("------------MIRROR------------")
    print(f": RORRIM\n{len(remaining_string)}")
    string_second = remaining_string if len(remaining_string) != 0 else "ytpmE"
    print(string_second)
    print(f"(RORRIM) ! ! ! (s)evisolpxE {disrupt_count}")


input_string = input("Enter Input (Normal, Mirror) : ").strip()
process_input(input_string)