from main import BooksCollector
import pytest


class TestBooksCollector:


    def test_add_new_book_only_name_added(self,collector):
        book_name = 'Властелин колец'
        collector.add_new_book(book_name)
        first_value = {'Властелин колец': ''}
        assert collector.books_genre == first_value


    def test_set_book_genre_name_exists_genre_added(self, add_book):
        add_book.set_book_genre('Властелин колец', 'Фантастика')
        assert add_book.books_genre['Властелин колец'] == 'Фантастика'


    def test_get_book_genre_name_return_genre(self, add_genre):
        assert add_genre.get_book_genre('Властелин колец') == 'Фантастика'


    def test_get_books_with_specific_genre_fantazy_genre_all_books(self, add_books):
        fantasy_books = add_books.get_books_with_specific_genre('Фантастика')
        assert fantasy_books == ['Властелин колец', 'Чапаев и Пустота', 'Дюна']


    def test_get_books_with_specific_genre_zero_books_genre_none(self, add_books):
        assert add_books.get_books_with_specific_genre('Приключения') == []


    def test_get_books_genre_all_books_showing(self, add_books):
        all_books = add_books.get_books_genre()
        assert len(all_books) == 6

    def test_get_books_for_children_fantasy_exists(self, add_books):
        childeren_books = add_books.get_books_for_children()
        assert 'Дюна' in childeren_books


    def test_get_books_for_children_horor_not_exists(self, add_books):
        childeren_books = add_books.get_books_for_children()
        assert 'Оно' not in childeren_books


    def test_add_book_in_favorites_same_book_no_duplicate(self, add_book_in_favorites):
        add_book_in_favorites.add_book_in_favorites('Властелин колец')
        assert add_book_in_favorites.favorites.count('Властелин колец') == 1


    def test_add_book_in_favorites_book_exists_added(self, add_book_in_favorites):
        assert 'Властелин колец' in add_book_in_favorites.favorites


    def test_delete_book_from_favorites_book_exists_deleted(self, add_book_in_favorites):
        add_book_in_favorites.delete_book_from_favorites('Властелин колец')
        assert 'Властелин колец' not in add_book_in_favorites.favorites


    def test_get_list_of_favorites_exists_books_added(self,add_books):
        favorite_books = ['Властелин колец', 'Чапаев и Пустота', 'Отель у погибшего альпиниста']
        for name in favorite_books:
            add_books.add_book_in_favorites(name)
        assert add_books.get_list_of_favorites_books() == favorite_books

        def test_get_list_of_favorites_exist_book_added(self,add_books):
        favorite_books = ['Властелин колец']
        for name in favorite_books:
            add_books.add_book_in_favorites(name)
        assert add_books.get_list_of_favorites_books() == favorite_books



        








    
        

