print("Xin Chao")
string="Chao mung den LabAI HaUI"
a=string[0:25]
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