#Herança é quando queremos tratar duas classes com relacionamento porém
#Não existe uma relação de evolução para ser usado Herança

from typing import List

class Book:
    def __init__(self, name):
         self.name = name

    def __str__(self):
        return f"Book {self.name}"

class BookShelf:
    def __init__(self, *books: List[Book]):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
    
book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)