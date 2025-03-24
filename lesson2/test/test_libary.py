
import pytest
from lesson2.my_libary import library
from lesson2.my_libary import book
my_lib=library.Library()
my_book = book.Book("מסומן", "רותי קפלר")
my_book1 = book.Book("BBB", "BB")
#הוספת ספר ריק לא נותן
def intialize():
    my_lib.add_user("תמי")
   # my_lib.add_book(my_book)
    my_lib.check_out_book("תמי",my_book)

@pytest.mark.parametrize("title,author", [("מסומן", "רותי קפלר"), ("שניה לפני האור", "רותי קפלר"), ("", "")])
def test_add_book(title, author):
    my_book = book.Book(title, author)
    assert my_lib.add_book(my_book)==True

#הוספת משתנה רגיל
@pytest.mark.user
def test_add_user():
    my_lib.add_user("תמי")
    assert my_lib.add_user("תמי")==True

# השאלת ספר לא קיים
@pytest.mark.book
def test_check_out_book():
    intialize()
    assert my_book.is_checked_out==True

@pytest.mark.book
@pytest.mark.user
#בדיקה שהספר באמת מוחזר
def test_return_book():
    intialize()
    my_lib.return_book("תמי",my_book)
    assert my_book.is_checked_out==False

#בדיקת אותיות קטנות וגדולות וחלקי ועוד
@pytest.mark.book
@pytest.mark.user
@pytest.mark.parametrize("title", ["bb", "b", ""])
def test_search_books(title):
   my_lib.add_book(my_book1)
   assert  my_lib.search_books(title)












