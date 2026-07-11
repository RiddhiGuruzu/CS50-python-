from twttr import shorten

def test_func_capital():
    assert shorten("TWITTER")== "TWTTR"

def test_func_small():
    assert shorten("twitter")== "twttr"

# type "python -m pytest test_twttr.py" in command window