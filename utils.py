def comparator(item1, item2):
    """
    do case-insensitive comparison of items
    :param item1: first str to compare
    :param item2: second str to compare
    :return: 1 if first comes after second in alphabetical order
             0 if both are equal
             -1 if first comes before second in alphabetical order
    """
    try:
        a = int(item1)
        b = int(item2)
    except ValueError:
        a = str.lower(item1)
        b = str.lower(item2)
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
