from fuel import gauge,convert

def test_convert():
    assert convert("3/4") == 75

def test_gauge():
    assert gauge(100) == "F"