from User import *


def main():
    lib=Library()
    
    lib.create_admin_account("abc@tech.com", "adad")
    lib.create_people_account("jhon@wick.com", "abc")

    usr=lib.people_login("jhon@wick.com", "abc")
    adm=lib.admin_login("abc@tech.com", "adad")

    lib.add_books(adm,"Pipilicka", 5)
    lib.add_books(adm,"Ognibina", 2)
    lib.add_books(adm,"Oporichita", 3)

    lib.check_books()

    usr.add_to_cart(lib.books[0])
    usr.add_to_cart(lib.books[1])

    usr.borrow_books()

    usr.cart_books()


if __name__=="__main__":
    main()