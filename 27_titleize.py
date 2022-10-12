def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words_list = phrase.split()

    for idx, word in enumerate(words_list):
        words_list[idx] = word.capitalize()

    return " ".join(words_list)
