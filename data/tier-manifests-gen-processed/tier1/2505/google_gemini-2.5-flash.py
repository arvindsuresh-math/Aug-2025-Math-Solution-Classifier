def solve():
    """Index: 2505.
    Returns: how many dollars Bob spent over the limit.
    """
    # L1
    necklace_cost = 34 # One necklace is worth $34
    book_more_expensive = 5 # $5 more expensive than the necklace
    book_cost = necklace_cost + book_more_expensive

    # L2
    total_cost = book_cost + necklace_cost

    # L3
    spending_limit = 70 # not to spend more than $70
    over_limit_amount = total_cost - spending_limit

    # FA
    answer = over_limit_amount
    return answer