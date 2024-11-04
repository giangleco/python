#Bai1
# set1=input("Nhap cac phan tu cua set 1:")
# set2=input("Nhap cac phan tu cua set 2:")
# set1= set(set1.split(','))
# print(set1)
# set2= set(set2.split(','))
# print(set2)
# #union la phuoc thuc de hop cac phan tu 
# hop=set1.union(set2)
# print(hop)
# #intersection la phuoc thuc de tim cac phan tu xuat hien tren cac set
# giao=set1.intersection(set2)
# print(giao)
# #difference la phuoc thuc de tim cac phan tu co trong set1 nhung khong co trong set2    
# tru=set1.difference(set2)
# print(tru)
# tru1=set2-set1
# print(tru1)
# # issubset() hoặc <= : trả về True nếu là tập con và ngược lại
# tapcon1=set1.issubset(set2)
# tapcon2=set2.issubset(set1)
# if tapcon1:
#     print("set1 la tap con cua set2")
# elif tapcon2:
#     print("set2 la tap con cua set1")
# else:
#     print("2 set khong phai la tap con cua nhau")
# # sorted(): trả về một list đã được sắp xếp tăng dần từ set được truyền vào (không sắp xếp set)
# print("Day da duoc sap xep se la 1 list:")
#sorted la ham sap xep theo thu tu tang dan
# print(sorted(hop))

#Bai2
# def count_word_frequency(text):
#   # Tách chuỗi thành các từ cach nhau dau space
#   words = text.split(" ")
#   # Tạo một từ điển(dictionary) để đếm tần suất
#   #dic co key-value
#   count = {}
#   for word in words:
#     #count[word] de lay gia tri tuong ung khoa world
#     # ham get de lay gia tri cua khoa world
#     #dem so lan lay gia tri cua khoa world
#     count[word] = count.get(word, 0) + 1
#   # Sắp xếp các từ theo thứ tự từ điển và in kết quả
#   #sorted la ham sap xep tang dan
#   #phuong thuc items() tra ve danh sach cac cap(key, value) tra ve la tuple
#   #in ra tung phan tu cua dictionary deu duoc sap xep theo thu tu alphabet
#   #phuong thuc sorted() deu sap xep theo thu tu alphabet
#   #word, count: Đây là hai biến được sử dụng để lưu trữ giá trị của mỗi phần tử trong quá trình lặp. Ở mỗi lần lặp, biến word sẽ nhận giá trị là key (khóa) của một phần tử trong từ điển, và biến count sẽ nhận giá trị là value (giá trị) tương ứng với key đó.
#   for word, count in sorted(count.items()):
#     #f la f-string -> chuyen vao cac doi so co trong {}
#     print(f"{word} {count}")
# text = input("Nhap van ban can check:")
# count_word_frequency(text)


#Bai3
# dicts={ # day la 1 dict gom key la cac so nguyen va value la dictionary
#     1:{'ma hoc phan':'IT6002','ten mon hoc':'Cau truc du lieu va giai thuat','so tin chi':'2'},
#     2:{'ma hoc phan':'IT6126','ten mon hoc':'He thng co so du lieu','so tin chi':'4'},
#     3:{'ma hoc phan':'IT6067','ten mon hoc':'kien truc may tinh va he dieu hanh','so tin chi':'3'},
#     4:{'ma hoc phan':'IT6120','ten mon hoc':'Lap trinh huong doi tuong','so tin chi':'3'}
# }

# # def check(s : list) -> list :
# #     arr=[]
# #     for i in range(len(s)):
# #         temp = s[i].split(' ')
# #         if (len(temp) > 5):
# #             arr.append(s[i])
# #     return arr
# #check ten mon hoc>5 va so tin chi >=3
# def check(dicts : dict) -> dict :
#     dict={}
#     for key, value in dicts.items(): # Duyet tung dict trong cac dicts
#         temp1 = value['ten mon hoc'].split(' ')
#         if (len(temp1) > 5 and int(value['so tin chi'])>= 3):
#             dict.update({key:value})
#     return dict
# # res = []
# # #dict long list 
# # arr = {'ten mon hoc' : [],
# #        'ma hoc phan':[]}
# # for i in range(1,5):
# #     cnt = 0
# #     for key, value in dicts[i].items():
# #         if (key == 'ten mon hoc'):
# #             arr['ten mon hoc'].append(value)
# #         if (cnt == 1 or cnt == len(dicts[i]) - 1):
# #             res.append([key, value])
# #         cnt += 1
# # res = dict(res)
# # print(arr)
# print(check(dicts))
# # def check(arr):
# #     for i in range(len(arr)):
# #         arr[i] = arr[i].split('')
# #         if arr[i] >5:
# #             return 
# def check(dicts:dict)->dict:
#     dict={}
#     for key,value in dicts.items():
#         temp=value['ten mon hoc'].split(' ')
#         if len(temp)>5 and int(value['so tin chi'])>=3:
#             dict.update({key:value})
#     return dict
# print(check(dicts))

#Bai 4
import random
import string
n=int(input("Nhap so sinh vien:"))
edu_mail={}
# string.ascii_letters: cac ki tu chu cai
# string.digits: Ca ki tu so
# string.punctuation: Cac ki tu dac biet
characters = string.ascii_letters + string.digits + string.punctuation
for i in range(1,n+1):
    Username=input(f"Username {i}:")
    while not len(Username)==10:
        print("Username phai co 10 ky tu")
        Username=input(f"Username {i}:")
    password = ''.join(random.choice(characters) for _ in range(10))
    #dict cua dict 
    edu_mail.update({i:{'Mail':Username+"@lab601.edu.vn", 'Password':password}})
print(edu_mail)


