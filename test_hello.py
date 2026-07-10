from hello import hello

def test_deafult():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Hemione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

