def solve():
    """Index: 350.
    Returns: the number of additional rolls of wrapping paper Chandler needs to sell.
    """
    # L1
    rolls_sold_grandmother = 3 # sold 3 rolls to his grandmother
    rolls_sold_uncle = 4 # sold 4 rolls to his uncle
    rolls_sold_neighbor = 3 # sold 3 rolls to a neighbor
    total_rolls_sold = rolls_sold_grandmother + rolls_sold_uncle + rolls_sold_neighbor

    # L2
    rolls_needed_total = 12 # needs to sell 12 rolls of wrapping paper
    rolls_remaining_to_sell = rolls_needed_total - total_rolls_sold

    # FA
    answer = rolls_remaining_to_sell
    return answer