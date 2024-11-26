from Book import Book
class BookStrore:
    def __init__(self) :
        self.listBooks=[]
    #Them sach
    def add_book(self,books):
        self.listBooks.append(books)
    #Xoa sach
    def remove_book(self,books):
        for i in self.listBooks:
            if i==books:
                self.listBooks.remove(i)
    def hienThi(self):
        for i in self.listBooks:
            print(i," ")
    #Tong doanh thu
    def total_revenu(self):
        total=0
        for i in self.listBooks:
            total+=Book.price
        return total