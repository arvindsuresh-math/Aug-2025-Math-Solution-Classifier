def solve():
    """Index: 2696.
    Returns: the number of books Patricia read.
    """
    # L1
    candice_books = 18 # If Candice read 18 books
    candice_multiplier = 3 # Candice read 3 times as many books as Amanda
    amanda_books = candice_books / candice_multiplier

    # L2
    kara_divisor = 2 # Kara read half the number of books that Amanda read
    kara_books = amanda_books / kara_divisor

    # L3
    patricia_multiplier = 7 # Patricia read 7 times the number of books that Kara read
    patricia_books = patricia_multiplier * kara_books

    # FA
    answer = patricia_books
    return answer