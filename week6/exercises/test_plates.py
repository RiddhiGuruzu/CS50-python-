from plates import is_valid


def test_twoletters():
    assert is_valid("CS50") == True

def test_max_sixchar():
    assert is_valid("OUTATIME") == False

def test_num():
    assert is_valid("CS50P") == False

def test_punctuation():
    assert is_valid("PI3.14") == False