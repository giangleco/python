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