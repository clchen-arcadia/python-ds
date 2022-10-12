def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    output_string = ""
    if type(num) != int:
        return None
    count = num
    if count < 0:
        return None
    while count > 0:
        output_string += phrase
        count -= 1
    return output_string
