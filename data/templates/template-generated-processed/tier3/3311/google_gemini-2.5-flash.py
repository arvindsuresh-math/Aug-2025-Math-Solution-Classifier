def solve():
    """Index: 3311.
    Returns: the amount of money Porter made for selling his previous painting.
    """
    # L1
    recent_painting_sale = 44000 # received $44,000 for the sale of his most recent painting
    less_amount = 1000 # $1000 less
    five_times_previous_painting = recent_painting_sale + less_amount

    # L2
    multiplier = 5 # five times more
    previous_painting_earnings = five_times_previous_painting / multiplier

    # FA
    answer = previous_painting_earnings
    return answer