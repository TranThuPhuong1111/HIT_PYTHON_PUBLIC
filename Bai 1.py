#*
n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
dem=0
x=int(input())
for i in lst:
    if i == x:
        dem +=1
print(dem)

#*
tmp=[8,5,4,0,1,3]
lst[1:7]=tmp
print(lst)

#*
print(max(lst))
print(min(lst))

#*
y=int(input())
lst.insert(0, y)
if lst==sorted(lst):
    print("TANG")
elif lst==sorted(lst, reverse= True):
    print("GIAM")
else:
    print("NO")

#*
lst2 =[]
tong=0
for i in lst:
    tong+=lst.append(tong)
print(lst2)

#*
lst3=[94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
print (sorted(lst3))
lst3_tmp=[]
for i in lst3:
    lst3_tmp.append(abs(i))
print (sorted(lst3_tmp))