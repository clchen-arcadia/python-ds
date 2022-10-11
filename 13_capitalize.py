def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    first_char_capital = phrase[:1].upper()
    return first_char_capital + phrase[1:]
