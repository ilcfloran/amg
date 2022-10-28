from backend.foobar import foobar


def test_foobar():
    assert foobar(1) == "1"
    assert foobar(3) == "foo"
    assert foobar(5) == "bar"
    assert foobar(15) == "foobar"
