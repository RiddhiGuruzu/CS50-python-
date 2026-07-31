from numb3rs import validate

def test_valid_ip():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True


def test_out_of_range():
    assert validate("275.3.6.28") is False
    assert validate("1.512.1.1") is False


def test_invalid_format():
    assert validate("cat") is False
    assert validate("192.168.001.1") is False