class CustomTypeError(Exception):
    def __init__(self, data_type: type) -> None:
        self.data_type = data_type

    def __str__(self) -> str:
        return f"{self.data_type} is not allowed. Only string"


def revers_word(word: str) -> str:
    if not isinstance(word, str):
        raise CustomTypeError(type(word))
    word_list = [letter for letter in word[::-1] if letter.isalpha()]
    new_word_list = []
    counter = 0
    for symbol in word:
        if not symbol.isalpha():
            new_word_list.append(symbol)
        else:
            new_word_list.append(word_list[counter])
            counter += 1
    new_word = ''.join(new_word_list)
    return new_word


def revers_text(text: str) -> str:
    if not isinstance(text, str):
        raise CustomTypeError(type(text))
    text_list = text.split(' ')
    new_text = ' '.join([revers_word(word=word) for word in text_list])
    return new_text


if __name__ == '__main__':
    cases = [
        ('abcd efgh', 'dcba hgfe'),
        ('a1bcd efg!h', 'd1cba hgf!e'),
        ('', ''),
    ]

    for text, reversed_text in cases:
        assert revers_text(text=text) == reversed_text
