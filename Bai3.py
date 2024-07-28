s1= input()
s2= input()
for i in range (-1, -len (s1)-1, -1):
    print (s1[i], end="")
print ("")
a=int (input())
b=int(input())
tmp=[]
if 0<=a<b<len(s2):
    tmp=s2[a:b +1][::-1]
tmp2=s2[:a]+tmp+s2[b+1:]
print (tmp2)
s3=s1[0:2]
print(s3)
s4=""
tmp2= len(s1) if len(s1)<len(s2) else len(s2)
for i in range (tmp2):
    s4+=s1[i]+s2[i]
if len(s2)-tmp2>0:
    print (s4+s2[tmp2::])
else:
    print(s4+ s1[tmp2::])
print(s1[0]+s2[1::])
print(s2[0]+s1[1::])

