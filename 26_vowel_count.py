def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!')
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    vowel_dict = {}
    for char in phrase:
        if char.lower() in vowel_set:
            vowel_dict[char.lower()] = vowel_dict.get(char.lower(), 0) + 1
    return vowel_dict
