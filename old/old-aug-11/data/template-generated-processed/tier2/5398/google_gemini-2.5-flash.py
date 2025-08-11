def solve():
    """Index: 5398.
    Returns: John's weight at the end.
    """
    # L1
    initial_weight = 220 # John weighs 220 pounds
    percentage_lost_decimal = 0.1 # lose 10% of his body weight
    weight_lost = initial_weight * percentage_lost_decimal

    # L2
    weight_gained = 2 # gains back 2 pounds
    net_loss_from_initial = weight_lost - weight_gained

    # L3
    final_weight = initial_weight - net_loss_from_initial

    # FA
    answer = final_weight
    return answer