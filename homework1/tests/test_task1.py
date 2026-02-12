import sys
import os

sys.path.append(os.path.abspath("src"))

def test_task1_output(capsys):
    import task1
    # capture what was printed
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"
