"""
 *tinh tong cac uoc so cua so cua so nguyen duong n
"""
print ("Nhap so nguyen duong n: ")
n=int (input())
sum=0
for i in range (1,n+1):
    if (n % i == 0):
        sum +=i
print("tong cac uoc so cua", n, "la: ", sum)    