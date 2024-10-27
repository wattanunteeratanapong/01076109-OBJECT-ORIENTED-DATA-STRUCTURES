# Chapter : 5 - item : 3 - Arthur กับเมืองลี้ลับ

# Arthur เป็นเด็กหนุ่มผู้หลงใหลในการเขียนโปรแกรมและการแก้ปริศนา หนึ่งวันหนึ่ง เขาได้รับ จดหมายลึกลับที่บอกว่าเขาถูกเชิญให้ไปที่เมืองปริศนา ซึ่งเป็นเมืองที่ถูกสร้างขึ้นมาจากโครงสร้างข้อมูล แบบ Linked List ทั้งหมด
# เมื่อ Arthur มาถึงเมืองปริศนา เขาพบว่าที่นี่มีการจัดการแข่งขันเขียนโปรแกรม โดยมีเป้าหมายคือ การแก้ปริศนาและช่วยเหลือผู้อยู่อาศัยในเมืองปริศนาให้พ้นจากปัญหาต่างๆ ที่เกิดขึ้นจากโครงสร้าง ข้อมูลที่ซับซ้อน Arthur ได้รับภารกิจแรกคือการแก้ปัญหาการจัดเรียงข้อมูลใน Linked List เพื่อทำให้ข้อมูลเรียงลำดับถูกต้อง
# ระดับความยาก : ง่ายคดๆ
# หมายเหตุ:
# - หลักการจัดวางคือ ตัวเลข, ตัวอักษรพิมพ์ใหญ่, ตัวอักษรพิมพ์เล็ก (คุ้นๆไหมมันคืออะไร?)
# - ไม่อนุญาตให้ใช้ .sort() เพราะตรวจ code นะจ๊ะ

# Test Case 1
# Enter unsorted Linked List: 5 4 3 2 1 0
# Before: 5 -> 4 -> 3 -> 2 -> 1 -> 0
# After : 0 -> 1 -> 2 -> 3 -> 4 -> 5

# Test Case 2
# Enter unsorted Linked List: 9 3 2 90 2 -1 3 8 2 3
# Before: 9 -> 3 -> 2 -> 90 -> 2 -> -1 -> 3 -> 8 -> 2 -> 3
# After : -1 -> 2 -> 2 -> 2 -> 3 -> 3 -> 3 -> 8 -> 9 -> 90

# Test Case 3
# Enter unsorted Linked List: z x y a c b
# Before: z -> x -> y -> a -> c -> b
# After : a -> b -> c -> x -> y -> z

# Test Case 4
# Enter unsorted Linked List: A g W Z b a P Q Y i l
# Before: A -> g -> W -> Z -> b -> a -> P -> Q -> Y -> i -> l
# After : A -> P -> Q -> W -> Y -> Z -> a -> b -> g -> i -> l

# Test Case 5
# Enter unsorted Linked List: settle nationalism note technique persist herd sculpture heat flatware jury
# Before: settle -> nationalism -> note -> technique -> persist -> herd -> sculpture -> heat -> flatware -> jury
# After : flatware -> heat -> herd -> jury -> nationalism -> note -> persist -> sculpture -> settle -> technique
