from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, email, password):
        self.email = email
        self.password = password


class People(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.cart = []

    def borrow_books(self):
        for book in self.cart:
            if book.copise > 0:
                book.copise -= 1
                print(f"{book.book_name} is borrowed.")
            else:
                print("No more copies left for borrow.")

    def cart_books(self):
        if len(self.cart) > 0:
            print("_________Books in cart_________")
            for book in self.cart:
                print(book.book_name)

    def add_to_cart(self, book):
        self.cart.append(book)


class Admin(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.books = []

    def publish_book(self, book):
        self.books.append(book)


class Books:
    def __init__(self, book_name, copise):
        self.book_name = book_name
        self.copise = copise


class Library:
    def __init__(self):
        self.peoples = []
        self.admins = []
        self.books = []

    def create_people_account(self, email, password):
        people = People(email, password)
        self.peoples.append(people)
        print("User Sign in successfull")

    def create_admin_account(self, email, password):
        admin = Admin(email, password)
        self.admins.append(admin)
        print("Admin Sign in successfull")

    def people_login(self, email, password):
        for people in self.peoples:
            if people.email == email and people.password == password:
                print("User logged in.")
                return people
            else:
                print("Invalid email or password!")
                return False

    def admin_login(self, email, password):
        for admin in self.admins:
            if admin.email == email and admin.password == password:
                print("Admin logged in.")
                return admin
            else:
                print("Invalid email or password!")
                return False

    def add_books(self, admin, book_name, copise):
        book = Books(book_name, copise)
        admin.publish_book(book)
        self.books.append(book)
        print(f"New book {book.book_name} is added.")

    def check_books(self):
        for book in self.books:
            if book.copise > 0:
                print(f'Book Name: {book.book_name} and Copies: {book.copise}')
                print("_________________________________")
