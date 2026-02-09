from datetime import datetime
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "log")


os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "School_Manager_System_log.txt")
def write_log(message: str):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time}] {message}\n")

class Item:
    _id_counter = 2000
    Item_list = []

    def __init__(self, name, price, category, year):
        self.__id = Item._id_generator()
        self.name = name
        self.__price = price
        self.category = category
        self.year = year

        self.add()

    @classmethod
    def _id_generator(cls):
        current_id = cls._id_counter
        cls._id_counter += 5
        return current_id

    @property
    def id(self):
        return self.__id

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    def add(self):
        Item.Item_list.append(self)
        print("Item added")
        write_log(f"Library Item ===> Item added (id : {self.id})")

    def remove(self):
        Item.Item_list.remove(self)
        print("Item removed")
        write_log(f"Library Item ===> Item removed (id : {self.id})")

    @classmethod
    def Item_count(cls):
        print(f"Item count is: {len(Item.Item_list)}")
        write_log(f"Library Item ===> Count requested (total : {len(Item.Item_list)})")

    @classmethod
    def search_by_id(cls, id):
        for i in cls.Item_list:
            if i.id == id:
                s = f"Found ==> ID: {i.id} - name: {i.name} - category: {i.category} - price: {i.price} - year: {i.year}"
                write_log(f"Library Item ===> Search success (id : {i.id})")
                print(s)
                return i
        print("Not found")
        write_log(f"Library Item ===> Search failed (id : {id})")
        return None

    def edit(self, n_name=None, n_price=None, n_category=None, n_year=None):
        if n_name is not None:
            self.name = n_name
        if n_price is not None:
            self.price = n_price
        if n_category is not None:
            self.category = n_category
        if n_year is not None:
            self.year = n_year

    @classmethod
    def show_all(cls):
        item_info = []
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- All Items -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        write_log("Library Item ===> Show all items requested")
        for i in cls.Item_list:
            info = f"Found ==> ID: {i.id} - name: {i.name} - category: {i.category} - price: {i.price} - year: {i.year}"
            item_info.append(info)
            print(info)
        return item_info


class Book(Item):
    def __init__(self, name, price, category, year, author, isbn, num_page):
        super().__init__(name, price, category, year)
        self.author = author
        self.isbn = isbn
        self.num_page = num_page

    def show(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- Book Info -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print(f"Book ID: {self.id}")
        print(f"Book name: {self.name}")
        print(f"Book price: {self.price}")
        print(f"Book category: {self.category}")
        print(f"Book year: {self.year}")
        print(f"Book Author: {self.author}")
        print(f"Book ISBN: {self.isbn}")
        print(f"Book Num Page: {self.num_page}\n")
        write_log(f"Library Item ===> Book info requested (id : {self.id})")

    def edit(self, n_name=None, n_price=None, n_category=None, n_year=None,
             n_author=None, n_isbn=None, n_page_num=None):
        super().edit(n_name=n_name, n_price=n_price, n_category=n_category, n_year=n_year)
        if n_author is not None:
            self.author = n_author
        if n_isbn is not None:
            self.isbn = n_isbn
        if n_page_num is not None:
            self.num_page = n_page_num
        print("Book edited")
        write_log(f"Library Item ===> Book edited (id : {self.id})")


class Magazine(Item):
    def __init__(self, name, price, category, year, num_page):
        super().__init__(name, price, category, year)
        self.num_page = num_page

    def show(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- Magazine Info -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print(f"Magazine ID: {self.id}")
        print(f"Magazine Name: {self.name}")
        print(f"Magazine Price: {self.price}")
        print(f"Magazine category: {self.category}")
        print(f"Magazine Num Page: {self.num_page}")
        print(f"Magazine year: {self.year}\n")
        write_log(f"Library Item ===> Magazine info requested (id : {self.id})")

    def edit(self, n_name=None, n_price=None, n_category=None, n_year=None,
             n_page_num=None):
        super().edit(n_name=n_name, n_price=n_price, n_category=n_category, n_year=n_year)
        if n_page_num is not None:
            self.num_page = n_page_num
        print("Magazine edited")
        write_log(f"Library Item ===> Magazine edited (id : {self.id})")


class DVD(Item):
    def __init__(self, name, price, category, year, duration, num_file):
        super().__init__(name, price, category, year)
        self.duration = duration
        self.num_file = num_file

    def show(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- DVD Info -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print(f"DVD ID: {self.id}")
        print(f"DVD Name: {self.name}")
        print(f"DVD Price: {self.price}")
        print(f"DVD category: {self.category}")
        print(f"DVD duration: {self.duration}")
        print(f"DVD num file: {self.num_file}")
        print(f"DVD year: {self.year}\n")
        write_log(f"Library Item ===> DVD info requested (id : {self.id})")

    def edit(self, n_name=None, n_price=None, n_category=None, n_year=None,
             n_duration=None, n_num_file=None):
        super().edit(n_name=n_name, n_price=n_price, n_category=n_category, n_year=n_year)
        if n_duration is not None:
            self.duration = n_duration
        if n_num_file is not None:
            self.num_file = n_num_file
        print("DVD edited")
        write_log(f"Library Item ===> DVD edited (id : {self.id})")


if __name__ == "__main__":

    print("\n--- Test 1: Create Items ---")
    b1 = Book("Harry Potter", 150, "Fantasy", 2001, "J.K.Rowling", "123456789", 450)
    m1 = Magazine("Science Weekly", 50, "Science", 2020, 40)
    d1 = DVD("Interstellar", 90, "Movie", 2014, 180, 2)

    print("\n--- Test 2: Show Items Individually ---")
    b1.show()
    m1.show()
    d1.show()

    print("\n--- Test 3: Show All Items ---")
    Item.show_all()

    print("\n--- Test 4: Search by ID ---")
    Item.search_by_id(b1.id)
    Item.search_by_id(9999)  # Not found

    print("\n--- Test 5: Edit Item (Base class edit) ---")
    b1.edit(n_category="Magic", n_page_num=500)
    b1.show()

    print("\n--- Test 6: Edit Price Using Property ---")
    b1.edit(n_price=200)
    print(f"New Price: {b1.price}")

    print("\n--- Test 7: Remove Item ---")
    d1.remove()
    Item.show_all()

    print("\n--- Test 8: Count Items ---")
    Item.Item_count()

    print("\n--- Test 9: Inheritance Check ---")
    print(isinstance(b1, Item))
    print(isinstance(m1, Item))
    print(isinstance(d1, Item))
    print(isinstance(b1, Book))
    print(isinstance(b1, Magazine))


