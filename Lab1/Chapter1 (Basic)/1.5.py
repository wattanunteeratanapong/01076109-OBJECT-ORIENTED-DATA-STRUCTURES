# Chapter : 1 - item : 5 - Countdown มหาสนุก

# อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ
# โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร

print("*** Fun with countdown ***")
numbers = list(map(int, input("Enter List : ").split()))

countdowns = []
current_countdown = []

for i in range(len(numbers)):
    if current_countdown and numbers[i] == current_countdown[-1] - 1:
        current_countdown.append(numbers[i])
        if numbers[i] == 1:
            countdowns.append(current_countdown)
            current_countdown = []
    elif numbers[i] == 1:
        countdowns.append([1])
    else:
        if current_countdown:
            current_countdown = []
        current_countdown.append(numbers[i])

if current_countdown and current_countdown[-1] == 1:
    countdowns.append(current_countdown)

print(f"[{len(countdowns)}, {countdowns}]")

# Time Complexity
# O(n)

# Space Complexity
# O(n)