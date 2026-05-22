from main import BooksCollector
import pytest


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture()
def add_book(collector):
    collector.add_new_book('Властелин колец')
    return collector


@pytest.fixture()
def add_genre(add_book):
    add_book.set_book_genre('Властелин колец', 'Фантастика')
    return add_book


@pytest.fixture()
def add_books(collector):
    books = [
        ('Властелин колец', 'Фантастика'),
        ('Чапаев и Пустота', 'Фантастика'),
        ('Дюна', 'Фантастика'),
        ('Оно', 'Ужасы'),
        ('Отель у погибшего альпиниста', 'Детективы'),
        ('Понедельник начинается в субботу', 'Комедии')
        ]
    for name, genre in books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector  


@pytest.fixture()
def add_book_in_favorites(add_book):
    add_book.add_book_in_favorites('Властелин колец')
    return add_book
