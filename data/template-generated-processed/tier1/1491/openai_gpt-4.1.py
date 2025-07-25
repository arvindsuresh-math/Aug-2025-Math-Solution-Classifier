def solve():
    """Index: 1491.
    Returns: the number of marbles remaining in the store after the sales.
    """
    # L1
    num_customers = 20 # Twenty customers
    marbles_per_customer = 15 # each bought 15 marbles
    marbles_sold = num_customers * marbles_per_customer

    # L2
    marbles_initial = 400 # 400 marbles remaining after the previous day's sales
    marbles_remaining = marbles_initial - marbles_sold

    # FA
    answer = marbles_remaining
    return answer