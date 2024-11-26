
class Book:
    def __init__(self,title,author,price) :
        self.title=title#ten sach
        self.author=author#ten tac gia
        self.price=price#Gia sach
    def gia(self):
        return self.price
#Lop doi tuong sach bia mem
class SoftCoverBook(Book):
    def __init__(self, title, author, price,discount):
        super().__init__(title, author, price)
        self.discount=discount
    #tra ve gia sach da duoc giam gia
    def calculate_discounted_price(price,discount):
        return price*(1-discount/100)
class HardCoverBook(Book):
    def __init__(self, title, author, price,weight):
        super().__init__(title, author, price)
        self.weight=weight
    def calculate_shipping_cost(weight):
        return weight*15000
    