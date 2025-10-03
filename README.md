# qa_python





Создано 14 методов-тестов, из них 4 параметризированных, включающих данные для проверки граничных значений или всех возможных вариантов. 
Всего запускается 24 теста.

Тестами покрыты все методы. 


    def __init__(self):
        test_init


    # добавляем новую книгу
    def add_new_book(self, name):
        test_add_new_book_name_length (5)
 

    # устанавливаем книге жанр
    def set_book_genre(self, name, genre):
        test_set_book_genre (4)


    # получаем жанр книги по её имени
    def get_book_genre(self, name):
        test_get_book_genre (2)


    # выводим список книг с определённым жанром
    def get_books_with_specific_genre(self, genre):
        test_get_books_with_specific_genre_list_not_empty
        test_get_books_with_specific_genre_list_empty
        test_get_books_with_specific_genre_genre_not_in_list


    # получаем словарь books_genre
    def get_books_genre(self):
        test_get_books_genre


    # возвращаем книги, подходящие детям
    def get_books_for_children(self):
        test_get_books_for_children_on_2books_per_genre


    # добавляем книгу в Избранное
    def add_book_in_favorites(self, name):
        test_add_book_in_favorites (3)


    # удаляем книгу из Избранного
    def delete_book_from_favorites(self, name):
        test_delete_book_from_favorites_present_book
        test_delete_book_from_favorites_missing_book
        test_delete_book_from_favorites_from_empty_list


    # получаем список Избранных книг
    def get_list_of_favorites_books(self):
        test_get_list_of_favorites_books 