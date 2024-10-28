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