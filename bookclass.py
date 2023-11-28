class Publisher:
    def __init__(self,name):
        self.pub=name
class Book(Publisher):
    def __init__(self,title,author,name):
        self.title=title
        self.author=author
        Publisher.__init__(self, name)
class Python(Book):
    def __init__(self,price,page,title,author,name):
        self.price=price
        self.page=page
        Book.__init__(self,title,author,name)
    def display(self):
        print("The title of the book:",self.title)
        print("The publisher:",self.pub)
        print("The name of the author:",self.author)
        print("The no.of pages:",self.page)
        print("The price of the book:",self.price)
book=Python(1200,320,"Alchemist","Pauhlo Coehlo","DC Books")
book.display()