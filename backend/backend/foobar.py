def foobar(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "foobar"
    if number % 3 == 0:
        return "foo"
    if number % 5 == 0:
        return "bar"
    return str(number)
