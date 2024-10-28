tuplet1=()
tuplet2=()
tuple1=('Hoang','Hung','Thien','Hieu','Cuong','Thang')
tuple2=('Dinh','Hung','Hieu','Pham','Le','Minh','Duy')
check2=[True] *len(tuple1)

# for i in range(len(tuple1)):
#     check = False # co xuat hien hay khong
#     for j in range(len(tuple2)):
#         if  tuple1[i]==tuple2[j]:
#             check = True
#             break
#     if  not check :
#         tuplet1+=(tuple1[i],)
#duyet tung phan tu
# for i in tuple1:
#    if i not in tuple2:
#         tuplet1+=(i,) 
for i in tuple1:
    check1 =True
    #enumerate la ham tach thanh 2 gia tri index va gia tri
    for idx,j in enumerate(tuple2):
        if i==j:
            check1=False
            check2[idx] = False
            break
    if check1:
        tuplet1+=(i,)
for idx,i in enumerate(check2):
    if i:
        tuplet2+=(tuple2[idx],)
print("#tuple1-tuple2",tuplet1,"\n","#tuple2-tuple1",tuplet2)# for i in tuple2:
#     check=True
#     for j in tuple1:
#         if i==j:
#             check=False
#             break
#     if check:
#         tuplet2+=(i,)
# print("#tuple2-tuple1",tuplet2)

