#Bai 1
# def say_hello():
#     print("Hello world!")
# say_hello()

#Bai 2
# def generate_laugh():
#     for i in range(0,5):
#         print("Ha")
# generate_laugh()

#Bai 3
# def tinh_tong(a,b:int)->int:
#     def kiem_tra_so_nguye(n):
#         if isinstance(n,int):
#             return True
#         else:
#             return False
#     if kiem_tra_so_nguye(a) and kiem_tra_so_nguye(b):
#         return a+b
#     else:
#         return "Khong hop le"
# a=int(input("Nhap so a:"))
# b=int(input("Nhap so b:"))
# tinh=tinh_tong(a,b)
# print(f"Tong cua so{a} va {b} la {tinh}:")

#Bai 4
# def chia_khuyen_mai(gia_moi, phan_tram_khuyen_mai):
#     def tinh_gia_sau_khuyen_mai(gia_moi, phan_tram_khuyen_mai):
#         return gia_moi * (1 - phan_tram_khuyen_mai / 100)
#     gia_sau_khuyen_mai = tinh_gia_sau_khuyen_mai(gia_moi, phan_tram_khuyen_mai)
#     return gia_sau_khuyen_mai
# # Gọi hàm chia_khuyen_mai
# gia_sau_khuyen_mai = chia_khuyen_mai(100, 20)
# print(gia_sau_khuyen_mai)  # Kết quả là: 80

#Bai 5
# def tim(n):
#     list=[]
#     for i in range(1,n+1):
#         if i%2==0:
#             list.append(i)
#     print(list)
# n=int(input("Nhap so nguyen n:"))
# tim(n)

#Bai 6
# def dem(s:str)->int:
#    s=s.split(" ")
#    return len(s)
# s=str(input("Nhap chuoi:"))
# print(dem(s))

#Bai 7
def tinh(n):
    def fibonacci(m):
        if m<=0:
            return 0
        elif m==1:
            return 1
        else:
            return fibonacci(m-1)+fibonacci(m-2)
    list=[]
    for i in range(n):
        list.append(fibonacci(i))
    
    return list
n=int(input("Nhap so nguyen n:"))
print(tinh(n))
    