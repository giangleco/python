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


