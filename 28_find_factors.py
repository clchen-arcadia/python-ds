def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    # from math import sqrt

    small_factors = []
    large_factors = []

    check_until = int(num ** 0.5 ) + 1

    for x in range(1, check_until):
        if num % x == 0:
            comp = num // x
            if x == comp:
                small_factors.append(x)
            else:
                small_factors.append(x)
                large_factors.append(comp)

    large_factors.reverse()

    small_factors.extend(large_factors)

    return small_factors
