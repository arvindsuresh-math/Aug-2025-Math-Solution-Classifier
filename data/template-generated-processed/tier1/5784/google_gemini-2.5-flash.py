def solve():
    """Index: 5784.
    Returns: the amount of change Jay received.
    """
    # L1
    book_cost = 25 # a book for $25
    pen_cost = 4 # a pen for $4
    ruler_cost = 1 # a ruler for $1
    total_spent = book_cost + pen_cost + ruler_cost

    # L2
    paid_amount = 50 # paid with a fifty-dollar bill
    change = paid_amount - total_spent

    # FA
    answer = change
    return answer