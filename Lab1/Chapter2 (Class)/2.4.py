# Chapter : 2 - item : 4 - nong saimai

# หาค่าฐานของอายุของน้องสายไหม ที่อายุ 20,21 ตลอดกาล
# เช่น
# hbd(65) = "saimai is just 21, in base 32!"
# hdb(21) = "saimai is just 21, in base 10!"
# hdb(8888) = "saimai is just 20, in base 4444!"

def hbd(age):
    sommai_age = 0
    base = 0
    results = []
    if age % 2 == 0:
        sommai_age = 20
    else:
        sommai_age = 21

    if sommai_age == 20:
        base = age / 2
    else:
        base = (age - 1) / 2
    results.append(f"saimai is just {sommai_age}, in base {int(base)}!")

    if results:
        return "\n".join(results)


year = input("Enter year : ")
print(hbd(int(year)))