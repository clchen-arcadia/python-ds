def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # NOTE first attempt using arrays, wrote better method with two pointers
    # list_phrase_cleaned = [char.lower() for char in phrase if char != " "]
    # list_phrase_reversed = list_phrase_cleaned.copy()
    # list_phrase_reversed.reverse()

    # original_word_cleaned = "".join(list_phrase_cleaned)
    # reversed_word = "".join(list_phrase_reversed)

    # return original_word_cleaned == reversed_word

    phrase_no_space_list = [char for char in phrase if char != " "]
    phrase_no_space = "".join(phrase_no_space_list)

    left = 0
    right = len(phrase_no_space) - 1
    while (left < right):
        if phrase_no_space[left].lower() != phrase_no_space[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True
