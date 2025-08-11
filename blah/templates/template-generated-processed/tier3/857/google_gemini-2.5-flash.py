def solve():
    """Index: 857.
    Returns: the total number of books her brother bought.
    """
    # L1
    sarah_paperback_books = 6 # 6 paperback books
    paperback_divisor = 3 # one-third as many paperback books
    brother_paperback_books = sarah_paperback_books / paperback_divisor

    # L2
    sarah_hardback_books = 4 # 4 hardback books
    hardback_multiplier = 2 # two times the number of hardback books
    brother_hardback_books = sarah_hardback_books * hardback_multiplier

    # L3
    total_brother_books = brother_paperback_books + brother_hardback_books

    # FA
    answer = total_brother_books
    return answer