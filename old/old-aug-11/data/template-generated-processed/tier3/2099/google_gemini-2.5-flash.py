def solve():
    """Index: 2099.
    Returns: the number of books Stu has.
    """
    # L1
    elmo_books = 24 # Elmo has 24 books
    elmo_multiplier = 3 # 3 times as many books as his sister, Laura
    laura_books = elmo_books / elmo_multiplier

    # L2
    laura_multiplier = 2 # twice as many books as her brother, Stu
    stu_books = laura_books / laura_multiplier

    # FA
    answer = stu_books
    return answer