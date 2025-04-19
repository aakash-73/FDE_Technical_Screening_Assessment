from sorter.dispatcher import sort

def test_standard():
    assert sort(50, 40, 30, 10) == "STANDARD"

def test_special_bulky():
    assert sort(200, 50, 50, 10) == "SPECIAL"

def test_special_heavy():
    assert sort(50, 50, 50, 25) == "SPECIAL"

def test_rejected():
    assert sort(200, 200, 200, 30) == "REJECTED"
