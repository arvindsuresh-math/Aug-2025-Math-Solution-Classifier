def solve():
    """Index: 113.
    Returns: the total number of marbles Baez ends up with.
    """
    # L1
    initial_marbles = 25 # Baez has 25 marbles
    loss_percent_decimal = 0.2 # loses 20% of them
    marbles_lost = initial_marbles * loss_percent_decimal

    # L2
    marbles_after_loss = initial_marbles - marbles_lost

    # L3
    friend_multiplier = 2 # gives her double the amount
    marbles_from_friend = marbles_after_loss * friend_multiplier

    # L4
    final_marbles = marbles_from_friend + marbles_after_loss

    # FA
    answer = final_marbles
    return answer