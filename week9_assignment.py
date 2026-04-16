from dataclasses import dataclass, field
@dataclass
class Book:
    title: str
    price : float
    copies : int 

    def value(self) -> float:
        return round(self.price * self.copies, 2)
    
@dataclass
class BookStore:
    name : str
    books: list[Book] = field(default_factory=list)
    total_stock_value: float=field (init=False)

    def __post_init__ (self):
        self.update_total_value()
    
    def update_total_value(self):
        self.total_stock_value = round(sum(book.value() for book in self.books), 2)

    def add_book(self, book: Book):
        self.books.append(book)
        self.update_total_value()

    def sell(self, title: str, qty: int) -> bool:
        for book in self.books:
            if book.title == title:
                if book.copies >= qty:
                    book.copies -= qty
                    total =0.0
                    for b in self.books:
                        total += b.value()
                        self.total_stock_value = round(total, 2)
                    return True
                return False
        return False
    
    def restock(self, title: str, qty: int):
        for book in self.books:
            if book.title == title:
                book.copies += qty
                self.total_stock_value = round(sum(b.value() for b in self.books), 2)
                break

    def report (self) -> str:
        report_text = f"{self.name} Catalog:\n"
        for b in self.books:
            report_text += f"  {b.title}: {b.copies} copies @ ${b.price} each\n"
        
        report_text += f"Total stock value: ${self.total_stock_value}"
        return report_text
    
b1 = Book("Python Basics", 34.99, 25)
b2 = Book("Data Science", 49.99, 15)
b3 = Book("Web Dev", 27.50, 40)

s = BookStore("PageTurn")
s.add_book(b1)
s.add_book(b2)
s.add_book(b3)

print(s.total_stock_value)
print(s.sell("Python Basics", 10))
print(s.sell("Python Basics", 20))
s.restock("Web Dev", 20)
print(s.report())




