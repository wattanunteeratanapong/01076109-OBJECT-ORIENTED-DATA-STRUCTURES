# Chapter : 2 - item : 3 - New Range

# ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการสร้าง range() ใหม่ขึ้นมาโดยใช้ function แค่ 1 function
# ถ้าหากเป็น 1 argument -> range(a)            | start = 0 , end = a , step = 1
# ถ้าหากเป็น 2 argument -> range(a, b)        | start = a , end = b , step = 1
# ถ้าหากเป็น 3 argument -> range(a, b, c)    | start = a , end = b , step = c

def new_range(*args):
    start = 0.0
    step = 1.0
    
    if len(args) == 1:
        end = float(args[0])
    elif len(args) == 2:
        start = float(args[0])
        end = float(args[1])
    elif len(args) == 3:
        start = float(args[0])
        end = float(args[1])
        step = float(args[2])
    else:
        raise TypeError(f"new_range expected at most 3 arguments, got {len(args)}")

    result = []
    current = start
    while (step > 0 and current < end) or (step < 0 and current > end):
        result.append(round(current, 12))
        current += step

    return tuple(result)

print("*** New Range ***")
input_data = input("Enter Input : ").split()
float_args = [float(i) for i in input_data]
print(new_range(*float_args))

# Time Complexity
# O(n)

# Space Complexity
# O(n)