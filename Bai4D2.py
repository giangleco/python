import math#thu vien toan hoc
a1,a2,b1,b2,c1,c2=map(float,input("Nhap toa do cua a,b,c: ").split())
#split(_) la phuong thuc tach xau ra thanh danh sach dang string ==> nhap tat ca
#ham map() la ham gan kieu nhieu phan tu cung 1 luc
a=math.sqrt(a1*2+a2*2)
b=math.sqrt(b1*2+b2*2)
c=math.sqrt(c1*2+c2*2)
if a<b:
    if b<c:
        print("Nha A gan truong nhat")
    elif c<b and a>c:
        print("Nha C gan truong nhat")
else:
    print("Nha B gan truong nhat")
            