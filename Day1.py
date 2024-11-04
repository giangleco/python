#Bai 1
print("Xin Chao")
string="Chao mung den LabAI HaUI"
a=string[0:25]
#Bai 2
print(a)
print("Khoa CNTT thuoc truong DH Cong nghiep Ha Noi -10 diem")
chuoi="Khoa CNTT thuoc truong DH Cong nghiep Ha Noi"
print("Cac chu in hoa trong chuoi la:")
for kytu in chuoi:
    if kytu.isupper():#kiem tra chu hien tai co la chu in hoa ko
        print(kytu)
print("Cac chu thuong trong chuoi la:")
for kytu in chuoi:
    if kytu.islower():#kiem tra chu hien tai co la chu thuong ko
        print(kytu)
check_bien="CNTT"
if check_bien in chuoi:
    print("Yes")
else:   
    print("No")
chuoi_moi=chuoi.swapcase()
print(chuoi_moi)

#Bai 3
for i in range(3):
    for j in range(5):
        print("*",end="")
    print()
print("  *  ")
for i in range(2):
    for j in range(5):
        print("*", end="")
    print()

#Bai4
a=input("Nhap vao so nguyen a: ")
b=input("Nhap vao so nguyen b: ") 
a=int (a)
b=int (b)
print("a + b=",a+b)
print("a - b=",a-b)
print("a * b=",a*b)
print("a / b=",a/b)
print("a // b=",a//b)
print("a % b=",a%b)
print("a^b=",a**b)

#Bai5
b=input("Full name: ")
a=input("Age:")
a=int(a)
c=input("Sex:")
d=input("Marital status:")
print(b,a," years old",c,d)