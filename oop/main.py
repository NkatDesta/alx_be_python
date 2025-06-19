from book_class import Book as MagicBook
from library_system import Book as BaseBook, EBook, PrintBook, Library
from polymorphism_demo import Shape, Rectangle, Circle
from class_static_methods_demo import Calculator

def test_magic_book():
    print("=== Testing Book class with magic methods ===")
    my_book = MagicBook("1984", "George Orwell", 1949)
    print(my_book)           
    print(repr(my_book))    
    del my_book             
    print()  


def test_library_system():
    print("=== Testing Library system with inheritance and composition ===")
    my_library = Library()
    classic_book = BaseBook("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)
    my_library.list_books()
    print()  

def test_polymorphism_demo():
    print("=== Testing Polymorphism Demo ===")
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
    print()  # blank line

def test_calculator():
    print("=== Testing Calculator static and class methods ===")
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
    print()  

def main():
    test_magic_book()
    test_library_system()
    test_polymorphism_demo()
    test_calculator()

if __name__ == "__main__":
    main()
