#bai1
def tong_cac_so(s):
    total = 0
    num = ''
    for char in s:
        if char.isdigit() or (char == '-' and not num):
            num += char
        else:
            if num:
                total += int(num)
                num = ''
    if num:
        total += int(num)
    return total
s = input("nhap chuoi di em a :")
result = tong_cac_so(s)
print(result)