def solve():
    """Index: 350.
    Returns: the number of rolls of wrapping paper Chandler still needs to sell.
    """
    # L1
    sold_to_grandmother = 3 # sold 3 rolls to his grandmother
    sold_to_uncle = 4 # sold 4 rolls to his uncle
    sold_to_neighbor = 3 # sold 3 rolls to a neighbor
    total_sold = sold_to_grandmother + sold_to_uncle + sold_to_neighbor

    # L2
    total_needed = 12 # needs to sell 12 rolls
    rolls_remaining = total_needed - total_sold

    # FA
    answer = rolls_remaining
    return answer