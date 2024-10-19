#ham tinh tien
def tinh(KHM,SLM,GT):
    if KHM:
        giam_gia=0.15
    else:
        giam_gia=0.1
    if 6 <= SLM <= 10:
        giam_gia+=0.05
    elif SLM >=10:
        giam_gia+=0.1
    if 10000<=GT<=50000:
        giam_gia+=0.08
    elif GT>50000:
        giam_gia+=0.15
    if KHM and SLM>10 and GT>100000:
        giam_gia+=0.2
    giam_gia=min(giam_gia,1)
    return GT-GT*giam_gia
KHM=input("Ban co phai la khach hang moi (yes/no)").lower()=="yes"
#lower() la ham chuyen doi ky tu sang kieu chu thuong 
SLM=int(input("So luong mua:"))
GT=int(input("So tien mua:"))
print("Tien sau khi giam gia la:",tinh(KHM,SLM,GT))

