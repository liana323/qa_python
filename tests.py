import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # жанр книги устанавливается правильно, если книга уже добавлена в словарь books_genre
    #указанный жанр входит в список genre
    def test_set_book_genre_valid_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        #добавляем книгy
        collector.add_new_book('Как же быть, как быть')

        #назначаем жанр
        collector.set_book_genre('Как же быть, как быть', 'Фантастика')

        #проверяем жанр книги установлен
        assert collector.get_book_genre('Как же быть, как быть') == 'Фантастика'


    #получаем жанр книги по её имени

    def test_get_book_genre_name_book_get_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгy
        collector.add_new_book('Как же быть, как быть')

        # назначаем жанр
        collector.set_book_genre('Как же быть, как быть', 'Фантастика')

        #проверяем жанр по книге
        assert collector.get_book_genre('Как же быть, как быть' ) == 'Фантастика'

    #выводим список книг с определённым жанром

    def test_get_books_with_specific_genre_list_of_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книги
        collector.add_new_book('Как же быть, как быть')
        collector.add_new_book('Быть умныч и хитрым')
        collector.add_new_book('А че че')

        # назначаем жанр
        collector.set_book_genre('Как же быть, как быть', 'Фантастика')
        collector.set_book_genre('Быть умныч и хитрым', 'Фантастика')
        collector.set_book_genre('А че че', 'Фантастика')

        #список книг с genre 'Фантастика'
        list_of_book_gender = collector.get_books_with_specific_genre('Фантастика')

        assert list_of_book_gender == ['Как же быть, как быть', 'Быть умныч и хитрым', 'А че че']

    #  возвращается корректный словарь
    def test_get_books_genre_list_of_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книги
        collector.add_new_book('Как же быть, как быть')
        collector.add_new_book('Быть умныч и хитрым')
        collector.add_new_book('А че че')

        # назначаем жанр
        collector.set_book_genre('Как же быть, как быть', 'Фантастика')
        collector.set_book_genre('Быть умныч и хитрым', 'Детективы')
        collector.set_book_genre('А че че', 'Ужасы')

        list_of_genre =collector.get_books_genre()

        assert list_of_genre == {
            'Как же быть, как быть': 'Фантастика',
            'Быть умныч и хитрым': 'Детективы',
            'А че че': 'Ужасы'
        }


    # возвращаем книги, подходящие детям
    def test_get_books_for_children_diff_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книги
        collector.add_new_book('Ляля')
        collector.add_new_book('Быть умныч и хитрым')
        collector.add_new_book('Малыш')

        # назначаем жанр
        collector.set_book_genre('Ляля', 'Мультфильмы')
        collector.set_book_genre('Быть умныч и хитрым', 'Ужасы')
        collector.set_book_genre('Малыш', 'Комедии')

        list_of_genre_age_rating = collector.get_books_for_children()

        assert list_of_genre_age_rating == [ 'Ляля', 'Малыш']

    #добавляем книгу в Избранное

    @pytest.mark.parametrize('books_add, expected_favorites', [
        (['Ляля', 'Быть умныч и хитрым'], ['Ляля', 'Быть умныч и хитрым']),
        (['Малыш'], ['Малыш']),
        (['Ляля', 'Малыш', 'Быть умныч и хитрым'], ['Ляля', 'Малыш', 'Быть умныч и хитрым'])])

    def test_add_book_in_favorites(self,books_add, expected_favorites):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книги
        for book in books_add:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        # добавление в избранное
        list_of_favorites = collector.get_list_of_favorites_books()

        assert list_of_favorites == expected_favorites

    @pytest.mark.parametrize('books_to_add, book_to_remove, expected_favorites', [
        (['Ляля', 'Быть умныч и хитрым'], 'Быть умныч и хитрым', ['Ляля']),
        (['Малыш', 'Ляля'], 'Малыш', ['Ляля']),
        (['Ляля', 'Быть умныч и хитрым', 'Малыш'], 'Ляля', ['Быть умныч и хитрым', 'Малыш'])
    ])
    def test_delete_book_from_favorites(self, books_to_add, book_to_remove, expected_favorites):
        collector = BooksCollector()

        for book in books_to_add:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        #формируем список из удаленных книг

        collector.delete_book_from_favorites(book_to_remove)
        list_of_favorites_after_delete = collector.get_list_of_favorites_books()

        assert list_of_favorites_after_delete == expected_favorites


    #получаем список Избранных книг
    def test_add_book_in_favorites_books_valid(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книги
        collector.add_new_book('Ляля')
        collector.add_new_book('Быть умныч и хитрым')
        collector.add_new_book('Малыш')

    # добавление в избранное
        collector.add_book_in_favorites('Ляля')
        collector.add_book_in_favorites('Малыш')

        list_of_favorites = collector.get_list_of_favorites_books()


        assert list_of_favorites == ['Ляля', 'Малыш']


