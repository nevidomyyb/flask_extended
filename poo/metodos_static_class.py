class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book ({self.name}, {self.book_type}, weighting {self.weight}g)>"
    
    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPES[0], weight + 100)

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.TYPES[1], weight)
    
    @staticmethod
    def static_method():
        pass
        # É usado quando a função não vai usar uma propriedade da classe

book = Book.hardcover("Harry Potter", 1400)
light = Book.paperback("Harry Potter", 1400)

print(book)
print(light)
    
