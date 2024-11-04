#Bai 1
import math#thu vien math 
while True:
  a=int(input("Nhap vao so nguyen duong n:"))
  if a>=0:
    break
tong=0
for i in range(1,a+1):
  tong+=i
print("tong= ",tong)
for i in range(1,a+1):
  if i%3==0:
    continue
  print(i)
tongsnt=0
#duyet cac phan tu 2 den n 
for i  in range(2,a+1):
    #duyet cac phan tu tu 2 den can cua n de kiem tra
    for j in range(2,int(math.sqrt(i)+1)):
      #kiemtra
      if(i%j==0): 
        i=0
    tongsnt+=i
print("Tong cac so nguyen to tu 1 den n la: ",tongsnt)
print("Ve tam giac sao deu:")
for i in range(1, a+1):
    for j in range(1, a+1-i):
        print("", end = " ")
    for k in range(1, i+1):
        print("*", end=" ")
    print()

#Bai 2
def MAX(check):
    MAX=check[0]
    for i in range(0,len(check)):
        if check[i]>check[0]:
            MAX=check[i]
    return MAX
def MIN(check):
    MIN=check[0]
    for i in range(0,len(check)):
        if check[i]<check[0]:
            MIN=check[i]
    return MIN
def check(check):
    for i in range(0,len(check)):
        for j in range(0,len(check)):
            if check[j] ==MAX(check) and check[i]==MIN(check):
               return j,i
a=[14, 2, 20 ,5, 25,13,30,24,50,0]
print(check(a))

#Bai 3
for i in range(1,101):
    tong=0
    for j in range(1,i//2+1):
        if i%j==0:
            tong+=j
        if tong==i:
            print(i, end=" ")
