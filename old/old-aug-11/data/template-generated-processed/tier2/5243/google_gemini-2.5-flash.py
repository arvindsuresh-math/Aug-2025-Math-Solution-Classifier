def solve():
    """Index: 5243.
    Returns: the amount of change Sara gets back.
    """
    # L1
    book_cost_1 = 5.5 # a book for 5.5£
    book_cost_2 = 6.5 # a book for 6.5£
    total_spent = book_cost_1 + book_cost_2

    # L2
    bill_given = 20 # a 20£ bill
    change_back = bill_given - total_spent

    # FA
    answer = change_back
    return answer