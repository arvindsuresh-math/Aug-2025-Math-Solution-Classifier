def solve():
    """Index: 1491.
    Returns: the number of marbles remaining in the store.
    """
    # L1
    num_customers = 20 # Twenty customers came into the store
    marbles_per_customer = 15 # each bought 15 marbles
    total_marbles_bought = num_customers * marbles_per_customer

    # L2
    initial_marbles = 400 # 400 marbles remaining after the previous day's sales
    marbles_remaining = initial_marbles - total_marbles_bought

    # FA
    answer = marbles_remaining
    return answer