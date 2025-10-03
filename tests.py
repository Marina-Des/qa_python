from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector


class TestBooksCollector:


# ----- ФИКСТУРА -----
# Одна, поэтому нет смысла сейчас выделять ее в отдельный файл.

    @pytest.fixture(autouse=True)
    def books_collector(self):
        self.books_collector= BooksCollector()

    

# ----- МЕТОДЫ-ТЕСТЫ -----


    def test_init (self):
        # data
        # - данных никаких, только созданный экземпляр
        # test
        assert self.books_collector.books_genre == {} and \
            self.books_collector.favorites == [] and \
            self.books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'] and \
            self.books_collector.genre_age_rating == ['Ужасы', 'Детективы']




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



#Твой комментарий, Екатерина: 
#"Нужно исправить: тест будет проходить, даже если set не работает. Ты заранее создаешь книгу с жанром"

#Нет, не будет. Здесь я создаю только одну книгу в списке - "книга в списке" с пустой строкой в значении. Она мне нужна, чтобы протестировать добавление жанра уже существующей книге. В предыдущей версии эта строка заедения одной книги была в фикстуре, я ее сюда перенесла.
#То есть, изначальные данные - одна книга в списке books_genre. 
#Дальше идет тест: запускается set_book_genre с 4мя наборами данных. Данные покрывают все 4 возможнх варианта: книга есть в списке или нет, присваеваемый жанр в списке genre или нет. 2 раза используем заведенную книгу, 2 раза используем значения из списка genre.


    @pytest.mark.parametrize ('name,genre,test_status', [
        ['книга_в_списке', 'Фантастика',True],
        ['книга_в_списке', 'Не Фантастика',False],
        ['книга_не_в_списке', 'Комедии',False],
        ['книга_не_в_списке', 'не Комедии',False]])
    def test_set_book_genre(self, name, genre, test_status):
        # data
        self.books_collector.books_genre['книга_в_списке']=''
        # test
        self.books_collector.set_book_genre(name,genre)
        assert (name in self.books_collector.books_genre and self.books_collector.books_genre.get(name)==genre) ==test_status 



    @pytest.mark.parametrize ('name,genre', [
        ['книга_в_списке_фантастика','Фантастика'], ['книга_не_в_списке', None]])
    def test_get_book_genre (self, name, genre):
        # data
        self.books_collector.books_genre['книга_в_списке_детектив']='детектив'
        self.books_collector.books_genre['книга_в_списке_фантастика']='Фантастика'
        self.books_collector.books_genre['книга_в_списке_ужасы']='ужасы'
        # test
        assert self.books_collector.get_book_genre(name) == genre


    def test_get_books_with_specific_genre_list_not_empty(self):
        # data
        for i in self.books_collector.genre:
            self.books_collector.books_genre['книга_1_'+ i]=i
            self.books_collector.books_genre['книга_2_'+ i]=i
        # test
        books_with_genre=self.books_collector.get_books_with_specific_genre('Комедии')
        assert (len(books_with_genre)==2) and ( (books_with_genre[0]=='книга_1_Комедии' and books_with_genre[1]=='книга_2_Комедии') or (books_with_genre[0]=='книга_2_Комедии' and books_with_genre[1]=='книга_1_Комедии') )


    def test_get_books_with_specific_genre_list_empty(self):
        # data
        # пустой список books_genre есть после фикстуры
        # test
        books_with_genre=self.books_collector.get_books_with_specific_genre('Комедии')
        assert books_with_genre==[]


    def test_get_books_with_specific_genre_genre_not_in_list(self):
        # data
        # в списке genre нет жанра "фОнтастика"
        self.books_collector.books_genre['книга_в_списке_детектив']='детектив'
        self.books_collector.books_genre['книга_в_списке_фантастика']='Фантастика'
        self.books_collector.books_genre['книга_в_списке_ужасы']='ужасы'
        # test
        books_with_genre=self.books_collector.get_books_with_specific_genre('фОнтастика')
        assert books_with_genre==[]
        

    def test_get_books_genre(self):
        # data
        self.books_collector.books_genre['книга_в_списке']=''
        self.books_collector.books_genre['книга_в_списке_фантастика']='Фантастика'
        # test
        assert self.books_collector.get_books_genre() == {'книга_в_списке': '', 'книга_в_списке_фантастика': 'Фантастика'}


    def test_get_books_for_children_on_2books_per_genre (self):
        # data
        for i in self.books_collector.genre:
            self.books_collector.books_genre['книга_1_'+ i]=i
            self.books_collector.books_genre['книга_2_'+ i]=i
        # test
        books_for_children=self.books_collector.get_books_for_children()
        assert (len(books_for_children)==6) and len({'книга_1_Ужасы', 'книга_2_Ужасы', 'книга_1_Детективы', 'книга_2_Детективы'} & set(books_for_children)) == 0


    @pytest.mark.parametrize ('book_name,test_status', [
        ['книга_в_списке', True], 
        ['книга_не_в_списке', False], 
        ['книга_в_списке_в_избранном', True]])
    def test_add_book_in_favorites(self, book_name, test_status):
        # data
        self.books_collector.books_genre['книга_в_списке']=''
        self.books_collector.books_genre['книга_в_списке_в_избранном']=''
        self.books_collector.favorites = ['книга_в_списке_в_избранном']
        # test
        self.books_collector.add_book_in_favorites(book_name)
        assert ((book_name in self.books_collector.favorites) and (self.books_collector.favorites.count(book_name)<=1) ) == test_status


    def test_delete_book_from_favorites_present_book (self):
        # data
        self.books_collector.favorites=['книга_в_избранном_1', 'книга_в_избранном_2']
        # test
        self.books_collector.delete_book_from_favorites ('книга_в_избранном_1')
        assert self.books_collector.favorites == ['книга_в_избранном_2']


    def test_delete_book_from_favorites_missing_book (self):
        # data
        self.books_collector.favorites=['книга_в_избранном_1', 'книга_в_избранном_2']
        # test
        self.books_collector.delete_book_from_favorites ('Книга_НЕ_в_избранном')
        assert self.books_collector.favorites == ['книга_в_избранном_1', 'книга_в_избранном_2']


    def test_delete_book_from_favorites_from_empty_list (self):
        # data
        # сейчас список favorites и так пуст, но вдруг поменяются первоначальные условия    
        self.books_collector.favorites=[]
        # test
        self.books_collector.delete_book_from_favorites('книга')
        assert self.books_collector.favorites==[]


    def test_get_list_of_favorites_books (self):
        # data
        self.books_collector.favorites=['книга_в_избранном_1', 'книга_в_избранном_2']
        # test
        fav_books=self.books_collector.get_list_of_favorites_books()
        assert fav_books == ['книга_в_избранном_1', 'книга_в_избранном_2']