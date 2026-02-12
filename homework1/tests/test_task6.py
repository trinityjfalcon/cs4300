import pytest
import importlib
import task6

def test_word_count(capsys):
    # reload module
    importlib.reload(task6)

    # capture what was printed
    captured = capsys.readouterr()

    expectedWordCount = 104

    assert str(expectedWordCount) in captured.out