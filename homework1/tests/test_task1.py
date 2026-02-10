def test_task1_output():
    import task1
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"
