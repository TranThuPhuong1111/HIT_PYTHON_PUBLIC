def so_hoan_hao(s):
    count = 0
    num = 19 
    while True:
        if sum(int(digit) for digit in str(num)) == 10:
            count += 1
            if count == s:
                return num
        num += 9  

s=int(input("nhap so :"))
result = so_hoan_hao(s)
print (result)


