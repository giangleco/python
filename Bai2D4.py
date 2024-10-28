import math
def MIN(check):
    MIN=check[0]
    for i in range(0,len(check)):
        if check[i]<check[0]:
            MIN=check[i]
    return MIN
while True:
    n=int(input("Nhap so nguyen duong n:"))
    if n>=1:
        break
list=[]
tinh=[]
for i in range(1,n+1):
    msv=(input("input msv person {}:".format(i)))
    name=(input("input name person {}:".format(i)))
    dem=int(input("input so buoi len lab person {}:".format(i)))
    list.append(msv)
    list.append(name)
    list.append(dem)
    tinh.append(dem)
for i in range(2,len(list),3):
    if MIN(tinh)==list[i]:
        print("MSV:", list[i-2], "\nName:", list[i-1], "\nSo buoi len lab:", list[i],"\nLa nguoi co so buoi len lab thap nhat")
print("Danh sach nhung nguoi len lab")