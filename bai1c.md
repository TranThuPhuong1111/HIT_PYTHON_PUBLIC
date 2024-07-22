a=int (input())
b=int(input())
c=int(input())
if a<=0 or b<=0 or c<=0:
    print("khong la tam giac")
elif a+b<=c or a+c<=b or b+c<=a:
    print("khong la tam giac")
elif a==b and b==c:
    print("tam giac deu")
elif a==b or b==c or c==a:
    print ("tam giac can")
elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
    print ("tam giac vuong")
elif a+b>c or b+c>a or c+a>b:
    print ("tam giac nhon")
else:
    print("tam giac tu") 