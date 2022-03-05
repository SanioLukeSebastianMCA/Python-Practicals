class Publisher:
    def __init__(self, name):
        self.name = name

    def show(self):
        pass


class Book(Publisher):
    def __init__(self, title, author, name):
        self.title = title
        self.author = author
        Publisher.__init__(self, name)

    def show(self):
        pass


class Python(Book):
    def __init__(self, price, nopage, title, author, name):
        self.price = price
        self.nopage = nopage
        Book.__init__(self, title, author, name)

    def show(self):
        print('Book title:', self.title)
        print('Author:', self.author)
        print('Publisher:', self.name)
        print('Price: (Rs.)', self.price)
        print('No of pages:', self.nopage)


P1 = Python(503.56, 452, 'Twinkle Digest - Limited Edition', 'Gabriel', 'Twinkle Digest')
P1.show()
