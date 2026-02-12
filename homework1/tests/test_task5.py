import pytest
from task5 import bookList, studentDict

def test_book_list():
    # tests if 6 items in list
    assert len(bookList) == 6

def test_first_three_books():
    # test splicing
    expected_books = ["The Poppy War by R.F. Kuang", "The Dragon Republic by R.F. Kuang", "Before the Coffee Gets Cold by Toshikazu Kawaguchi"]
    assert bookList[0:3] == expected_books

def test_dict_length():
    assert len(studentDict) == 6

def test_student_ids():
    expectedDict = {
        "Shoobert Magoo": 101,
        "Bobert McGee": 102,
        "Muffin Man": 103,
        "Jimbob Borito": 104,
        "Snoopy Dawg": 105,
        "Abo Rito": 106
    }
    assert studentDict == expectedDict