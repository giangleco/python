import math
class hanghoa:
    def __init__(self,tenHang,donGia,soLuong):
        self.tenHang=tenHang
        self.donGia=donGia
        self.soLuong=soLuong
    def giaSP(donGia,soLuong):
        return round(donGia*soLuong,2)
class nhaCC:
    def __init__(self,maNCC,tenNCC,diaChi):
        self.maNCC=maNCC
        self.tenNCC=tenNCC
        self.diaChi=diaChi
class phieu(nhaCC):
    def __init__(self, maNCC=None, tenNCC=None, diaChi=None,maPhieu=None,ngayLap=None):
        super().__init__(maNCC, tenNCC, diaChi)
        self.maPhieu=maPhieu
        self.ngayLap=ngayLap
    def nhapPhieu(self):
        self.maPhieu=input("Nhap ma phieu : ")
        self.maNCC=input("Nhap ma nha cung cap : ")
        self.ngayLap=input("Nhap ngay lap : ")
        self.tenNCC=input("Nhap ten nha cung cap : ")
        self.diaChi=input("Nhap dia chi : ")
        sosp=int(input("Nhap so san pham:"))
        self.list=[]
        for i in range(sosp):
            tenHang=str(input("Ten hang:"))
            donGia=float(input("Don gia:"))
            soLuong=int(input("So luong:"))
            self.list.append(hanghoa(tenHang,donGia,soLuong))
    def inPhieu(self):
        for i in range(50):
            print("==",end='')
        print("\n")
        print("                                       PHIEU NHAP HANG")
        print("Ma phieu:",self.maPhieu,"                                                            Ngay lap:",self.ngayLap)
        print("Ma NCC  :",self.maNCC,"                                                             Ten NCC:",self.tenNCC  )
        print("Dia chi :",self.diaChi)
        for i in range(50):
            print("--",end="")
        print("\n")
        print("|        Ten hang           |        Don gia      |       So luong      |       Thanh tien        |")
        TongTien=0
        for i in self.list:
            thanhtien=hanghoa.giaSP(i.donGia,i.soLuong)
            TongTien=TongTien+thanhtien
            print("         ",i.tenHang,"                        ",i.donGia,"                    ",i.soLuong,"                     ",thanhtien,"         ")
        print("                                                                 Tong thanh tien               ",TongTien)
if __name__ == "__main__":       
    phieunhap=phieu()
    phieunhap.nhapPhieu()
    phieunhap.inPhieu()


        
        
        