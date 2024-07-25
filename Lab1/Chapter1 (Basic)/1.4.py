# Chapter : 1 - item : 4 - Game Minesweeper

# สร้างฟังก์ชันที่รับ input เป็น list(5x5) ของ # และ - โดยแต่ละแฮช (#) แทนทุ่นระเบิดและแต่ละขีด (-) แทนจุดที่ไม่มีทุ่นระเบิด ให้ return list ที่แต่ละขีดถูกแทนที่ด้วยตัวเลขที่ระบุจำนวนของทุ่นระเบิดที่อยู่ติดกับจุดนั้น (แนวนอนแนวตั้งและแนวทแยงมุม)

def num_grid(lst):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    rows = len(lst)
    cols = len(lst[0])

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if lst[i][j] == '#':
                result[i][j] = '#'
                continue

            count_mines = 0
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < rows and 0 <= nj < cols and lst[ni][nj] == '#':
                    count_mines += 1

            result[i][j] = str(count_mines)

    return result

print("*** Minesweeper ***")
input_str = input("Enter input(5x5) : ")
print()
print()

lst_input = [row.split() for row in input_str.split(',')]
for row in lst_input:
    print(row)
print()
print()

result_grid = num_grid(lst_input)
for row in result_grid:
    print(row)

# Time Complexity
# O(n²)

# Space Complexity
# O(n²)