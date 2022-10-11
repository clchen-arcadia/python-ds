def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    #switch_case = [char for char in phrase]
    switch_case = list(phrase)
    output_string = ""
    for char in switch_case:
        if char.lower() == to_swap.lower():
            if char.islower():
                output_string += char.upper()
            else:
                output_string += char.lower()
        else:
            output_string += char

    return output_string
