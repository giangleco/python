#Bai1
# while True:
#     n=int(input("Nhap so cong tac vien:"))
#     if n>=2:
#         break
# list=[]
# tinh=[]
# for i in range(1,n+1):
#     msv=(input("input msv person {}:".format(i)))
#     name=(input("input name person {}:".format(i)))
#     diem=float(input("input diem so cua person {}:".format(i)))
#     list.append([msv,name,diem])
#     tinh.append(diem)
#ham sorte la ham sap xep mac dinh cua sorted la tang dan neu muon giam dan thi dua reverse=Tre
#sorted_list=sorted(list,key=lambda item:item[2],reverse=True)
# for i in range(3):
#     print(sorted_list[i])

#Bai 2
# import re
# def check(s:str)-> bool:
#     if len(s)>=6 and re.search("[a-z]",s) and re.search("[0-9]",s) and not re.search("^a-z0-9",s):
#         return True
#     else:
#         return False
# n=int(input("Nhap so chuoi:"))
# list=[]
# dem=0
# for i in range(1,n+1):
#     n=str(input(f"Nhap chuoi {i}:"))
#     list.append(n)
#     if check(n):
#         dem+=1
#     else:
#         continue
# print(dem)
# print(list)

#Bai 3
# mangt1=()
# mangt2=()
# mang1=('tai','thuy','thach','truong','tien')
# mang2=('hai','tai','nhat minh', 'cao minh','dang anh','hung','truong')
# for i in mang1:
#     if i not in mang2:
#         mangt1+=(i,)
# print(mangt1)
# for i in range(len(mang2)):
#     check=False
#     for j in range(len(mang1)):
#         if mang2[i]==mang1[j]:
#             check=True
#             break
#     if not check:
#         mangt2+=(mang2[i],)
# print(mangt2)
#Bai 4
chuoi1=str(input("Nhap chuoi 1: "))
chuoi2=str(input("Nhap chuoi 2: "))
if len(chuoi1)>len(chuoi2):
    chuoi1 = chuoi1[len(chuoi1) - len(chuoi2):]
    a=chuoi1+chuoi2
elif len(chuoi1)<len(chuoi2):
    chuoi2 = chuoi2[len(chuoi2) - len(chuoi1):]
    a=chuoi1+chuoi2
else:
    a=chuoi1+chuoi2
print(a)

