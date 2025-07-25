def solve():
    """Index: 344.
    Returns: the initial number of marbles Archie started with.
    """
    # L1
    marbles_left = 20 # If he has 20 left
    half_lost_multiplier = 2 # loses half down a sewer
    marbles_before_sewer_loss = marbles_left * half_lost_multiplier

    # L2
    percent_lost_to_street = 60 # loses 60% of them into the street
    remaining_after_street_loss_decimal = 0.4 # from solution text: 40/.4
    initial_marbles = marbles_before_sewer_loss / remaining_after_street_loss_decimal

    # FA
    answer = initial_marbles
    return answer