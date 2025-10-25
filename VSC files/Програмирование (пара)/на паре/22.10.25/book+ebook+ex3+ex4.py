from datetime import datetime
from abc import ABC, abstractmethod

class Printable(ABC):

    @abstractmethod
    def print_info(self):
        pass

class book(Printable):
    category = "General"

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
    
    def description(self) -> str:
        return f"{self.title} - {self.author}, {self.year} года"

    def print_info(self) -> str:
        return f"{self.title}"

    def __str__(self):
        return self.print_info()

    def __eq__(self, other):
        return isinstance(other, book) and (self.title == other.title and self.author == other.author)

    @property
    def age(self):
        return datetime.now().year - self.year

    @age.setter
    def age(self, value):
        self.year = datetime.now().year - value

    @classmethod
    def from_string(cls, data):
        title, author, year = data.split(";")
        return cls(title, author, int(year))

class ebook(book):
    
    def __init__(self, title: str, author: str, year: str, format: str):
        super().__init__(title, author, year)
        self.format = format

    def info(self) -> str:
        return f"{self.title} - {self.author}, {self.year} года, Размещено в формате {self.format}"

    @classmethod
    def from_string(cls, data):
        title, author, year, format = data.split(";")
        return cls(title, author, int(year), format)

work = book("Превращение", "Франц Кафка", 1912)
work1 = ebook("Превращение", "Франц Кафка", 1912, "epub")

print(work1)

print(work == work1)

print(work1.age)

book3 = ebook.from_string("Превращение;Франц Кафка;1912;pdf")

print(book3)