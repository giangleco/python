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