def solve():
    """Index: 2505.
    Returns: the number of dollars Bob spent over his limit.
    """
    # L1
    necklace_price = 34 # necklace is worth $34
    book_more_than_necklace = 5 # book is $5 more expensive than the necklace
    book_price = necklace_price + book_more_than_necklace

    # L2
    total_spent = book_price + necklace_price

    # L3
    spending_limit = 70 # decided not to spend more than $70
    over_limit = total_spent - spending_limit

    # FA
    answer = over_limit
    return answer