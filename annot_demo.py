def say_something(number: int, word: str) -> str:
    word = word.capitalize()
    return word * number


def get_string(string: str, number: int) -> str:
    return string * number


print(get_string.__annotations__)