from BookStore import *
from Book import *
if __name__=="__main__":
    danhsach=BookStrore()
    sachmem=SoftCoverBook("Toi tai gioi ban cung the","Adam Koo",300,50)
    sachcung=HardCoverBook("Me yeu con","Trong Hieu",400,3)
    sachxoa=Book("Sach","Tacgia","350")
    danhsach.add_book(sachmem)
    danhsach.add_book(sachcung)
    danhsach.add_book(sachxoa)
    danhsach.hienThi()
    danhsach.remove_book(sachxoa)
    danhsach.hienThi()
    print("Gia sach mem la:",SoftCoverBook.calculate_discounted_price(sachmem.price,sachmem.discount))
    print("Phi ship voi sach cung la:",round(HardCoverBook.calculate_shipping_cost(sachcung.weight),1))
