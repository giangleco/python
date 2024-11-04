#Bai 1
a=int(input("So ban duoc thuong la:"))
b=int(input("So hop qua ma thay co la:"))
c=int(input("So tui qua co trong hop la:"))
if c*b%a==0:
    print("Chia deu duoc cho cac ban")
else:
    print("Khong chia deu duoc cho cac ban") 

#Bai 2
a=int(input("Nhap diem tong ket mon tieng anh:"))
if a>=8.5:
    print("Xep loai: A")
elif 7<=a<=8.49:
    print("Xep loai: B")
elif 5<=a<=6.99:
    print("Xep loai: C")
elif 4<=a<=4.99:
    print("Xep loai: D")
else:
    print("Xep loai: F =>> Ban danh mat 3.112.500")
    
#Bai 3
a=float(input("Nhap so a:"))
b=float(input("Nhap so b:"))
print((a>b)and"YES"or"NO")

#Bai 4

#Bai5
print("SO BUOC TOI 1")
while True:
    a=int(input("Nhap so nguyen duong n:"))
    if a>=0:
        break
tong=0
while a!=1:
    if a%2==0:
        a//=2
    else:
        a=a*3+1
    tong+=1
print(tong)

#Bai 6
def tim(chieucao):
    chieucao1=0
    #ham len() la ham dem so phan tu 
    for i in range(1,len(chieucao)):
        if chieucao[i]>chieucao[chieucao1]:
            chieucao1=i
    return chieucao1
#Nhap chieu cao cac nguoi
a=float(input("Nhap chieu cao cua An:"))
b=float(input(("Nhap chieu cao cua Linh:")))
c=float(input("Nhap chieu cao cua Duc:"))
d=float(input("Nhap chieu cao cua Nam:"))
#tao ham chieu cao
chieucao=[a,b,c,d]
#tao ham ten
name=["An","Linh","Duc","Nam"]
nguoicaonhat=tim(chieucao)
print(name[nguoicaonhat])

