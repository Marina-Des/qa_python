from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
"""    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2
"""


class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.fixture(autouse=True)
    def books_collector(self):
        self.books_collector= BooksCollector()
        self.books_collector.books_genre['книга_в_списке']=''
        self.books_collector.books_genre['книга_в_списке_фантастика']='Фантастика'
        return self.books_collector
    

    @pytest.fixture(autouse=False)
    def books_collector_with_2books_per_genre(self):
        self.books_collector.books_genre={}
        for i in self.books_collector.genre:
            self.books_collector.books_genre['книга_1_'+ i]=i
            self.books_collector.books_genre['книга_2_'+ i]=i

    
    @pytest.fixture(autouse=False)
    def book_collector_with_1book_in_favorites(self):
        self.books_collector.books_genre['книга_в_списке_в_избранном']=''
        self.books_collector.favorites = ['книга_в_списке_в_избранном']


    @pytest.mark.parametrize ('book_name, test_status', [
        ['', False], 
        ['a', True], 
        ['a'*39, True], 
        ['a'*40, True], 
        ['a'*41, False]])
    def test_add_new_book_name_length(self, book_name, test_status):
        #bc=BooksCollector()
        self.books_collector.add_new_book(book_name)
        assert (book_name in self.books_collector.books_genre) ==test_status

    # def test_add_new_book_add_existent_book(self): 
    # сначала надо уточнить целевое поведение метода. Ничего не делает? Выдает сообщение? Обнуляет жанр?


    @pytest.mark.parametrize ('name,genre,test_status', [
        ['книга_в_списке', 'Фантастика',True],
        ['книга_в_списке', 'Не Фантастика',False],
        ['книга_не_в_списке', 'Комедии',False],
        ['книга_не_в_списке', 'не Комедии',False]])
    def test_set_book_genre(self, name, genre, test_status):
        self.books_collector.set_book_genre(name,genre)
        assert (name in self.books_collector.books_genre and self.books_collector.books_genre.get(name)==genre) ==test_status 


    @pytest.mark.parametrize ('name,genre', [
        ['книга_в_списке_фантастика','Фантастика'], ['книга_не_в_списке', None]])
    def test_get_book_genre (self, name, genre):
        assert self.books_collector.get_book_genre(name) == genre


    def test_get_books_with_specific_genre_list_not_empty(self, books_collector_with_2books_per_genre):
        books_with_genre=self.books_collector.get_books_with_specific_genre('Комедии')
        assert (len(books_with_genre)==2) and ( (books_with_genre[0]=='книга_1_Комедии' and books_with_genre[1]=='книга_2_Комедии') or (books_with_genre[0]=='книга_2_Комедии' and books_with_genre[1]=='книга_1_Комедии') )


    def test_get_books_with_specific_genre_list_empty(self):
        self.books_collector.books_genre={}
        books_with_genre=self.books_collector.get_books_with_specific_genre('Комедии')
        assert books_with_genre==[]


    def test_get_books_with_specific_genre_genre_not_in_list(self):
        books_with_genre=self.books_collector.get_books_with_specific_genre('фОнтастика')
        assert books_with_genre==[]

    def test_get_books_genre(self):
        assert self.books_collector.get_books_genre() == {'книга_в_списке': '', 'книга_в_списке_фантастика': 'Фантастика'}


    def test_get_books_for_children_on_2books_per_genre (self, books_collector_with_2books_per_genre):
        books_for_children=self.books_collector.get_books_for_children()
        assert (len(books_for_children)==6) and len({'книга_1_Ужасы', 'книга_2_Ужасы', 'книга_1_Детективы', 'книга_2_Детективы'} & set(books_for_children)) == 0


    @pytest.mark.parametrize ('book_name,test_status', [
        ['книга_в_списке', True], 
        ['книга_не_в_списке', False], 
        ['книга_в_списке_в_избранном', True]])
    def test_add_book_in_favorites(self, book_name, test_status, book_collector_with_1book_in_favorites):
        self.books_collector.add_book_in_favorites(book_name)
        assert ((book_name in self.books_collector.favorites) and (self.books_collector.favorites.count(book_name)<=1) ) == test_status



