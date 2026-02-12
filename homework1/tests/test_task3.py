# builtins for the input() function
import builtins
import importlib

def test_positive(monkeypatch, capsys):
    # simulate user entering 1
    monkeypatch.setattr(builtins, "input", lambda _: "1")

    # runs script again with input
    import task3
    importlib.reload(task3)

    # capture what was printed
    captured = capsys.readouterr()

    assert "1.0 is positive" in captured.out

def test_negative(monkeypatch, capsys):
    # simulate user entering -2
    monkeypatch.setattr(builtins, "input", lambda _: "-2")

    # runs script again with input
    import task3
    importlib.reload(task3)

    # capture what was printed
    captured = capsys.readouterr()

    assert "-2.0 is negative" in captured.out

def test_zero(monkeypatch, capsys):
    # simulate user entering 0
    monkeypatch.setattr(builtins, "input", lambda _: "0")

    # runs script again with input
    import task3
    importlib.reload(task3)

    # capture what was printed
    captured = capsys.readouterr()

    assert "The number is zero" in captured.out

def test_primes(monkeypatch, capsys):
    # simulate user entering 1
    monkeypatch.setattr(builtins, "input", lambda _: "1")

    # runs script again for prime
    import task3
    importlib.reload(task3)

    # capture what was printed
    captured = capsys.readouterr()

    expected_prime = ["1", "2", "3", "5", "7", "11", "13", "17", "19", "23"]

    # check if each expected prime number is in output
    for prime in expected_prime:
        assert prime in captured.out

def test_sum(monkeypatch, capsys):
    # simulate user entering 1
    monkeypatch.setattr(builtins, "input", lambda _: "1")

    # runs script again for sum
    import task3
    importlib.reload(task3)

    # capture what was printed
    captured = capsys.readouterr()

    # check if sum is 5050
    assert "5050" in captured.out