def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    from collections import Counter
    counter = Counter(nums)
    items = counter.items()
    max = 0
    largest_tuple_count = ()
    for tuple in items:
        if tuple[1] > max:
            max = tuple[1]
            largest_tuple_count = tuple
    return largest_tuple_count[0]
