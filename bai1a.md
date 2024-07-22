"""
 *tinh tong cua cac chu so cua mot so nguyen duong n 
 *
 *param n: so nguyen duong
 *return
"""
def totalDigitsOfNumber(n):
    total=0;
    while (n>0):
        total =total +n%10;
        n=int (n/10);
    return total;
n=int(input("nhap so nguyen duong n ="));
print ("tong cac chu so cua", n, "la", totalDigitsOfNumber(n));

