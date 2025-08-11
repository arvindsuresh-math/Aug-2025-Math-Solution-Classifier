def solve():
    """Index: 113.
    Returns: the number of marbles Baez ends up with.
    """
    # L1
    initial_marbles = 25 # Baez has 25 marbles
    lost_percent = 0.2 # loses 20% of them
    marbles_lost = initial_marbles * lost_percent

    # L2
    marbles_after_loss = initial_marbles - marbles_lost

    # L3
    double_factor = 2 # double the amount
    marbles_given = marbles_after_loss * double_factor

    # L4
    final_marbles = marbles_given + marbles_after_loss

    # FA
    answer = final_marbles
    return answer