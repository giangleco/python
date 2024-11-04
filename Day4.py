#Bai 1
while True:
    n=int(input("Nhap so nguyen 5<=n<=80:"))
    if 5<=n<=80:
        break
x=int(input("Nhap so nguyen x can kiam tra:"))
list=[]
check=0
print("Nhap ca phan tu cua list")
for i in range(n):
    so=int(input("Nhap phan tu thu {}: ".format(i+1)))
    list.append(so)
    if so==x:
        check+=1
print("So phan tu {} co trong list la: ".format(x), check)
list.insert(0,1)
list.append(0)
for i in range(n+2):
    print(list[i],end=" ")
N=len(list)
L=[]
#neu i<2 thi L[i]=1 ko thi ...
L=[1 if i<2 else L[i-1]+L[i-2] for L[i] in range(N)]
print(L)
"""van chua chay duoc fibonacy"""

#Bai 2
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

#Bai 3
tuplet1=()
tuplet2=()
tuple1=('Hoang','Hung','Thien','Hieu','Cuong','Thang')
tuple2=('Dinh','Hung','Hieu','Pham','Le','Minh','Duy')
check2=[True] *len(tuple1)

# for i in range(len(tuple1)):
#     check = False # co xuat hien hay khong
#     for j in range(len(tuple2)):
#         if  tuple1[i]==tuple2[j]:
#             check = True
#             break
#     if  not check :
#         tuplet1+=(tuple1[i],)
#duyet tung phan tu
# for i in tuple1:
#    if i not in tuple2:
#         tuplet1+=(i,) 
for i in tuple1:
    check1 =True
    #enumerate la ham tach thanh 2 gia tri index va gia tri
    for idx,j in enumerate(tuple2):
        if i==j:
            check1=False
            check2[idx] = False
            break
    if check1:
        tuplet1+=(i,)
for idx,i in enumerate(check2):
    if i:
        tuplet2+=(tuple2[idx],)
print("#tuple1-tuple2",tuplet1,"\n","#tuple2-tuple1",tuplet2)# for i in tuple2:
#     check=True
#     for j in tuple1:
#         if i==j:
#             check=False
#             break
#     if check:
#         tuplet2+=(i,)
# print("#tuple2-tuple1",tuplet2)

