def solve():
    """Index: 2393.
    Returns: how many more pounds Patty weighs than Robbie now.
    """
    # L1
    robbie_weight = 100 # Robbie weighs 100 pounds
    patty_weight_factor = 4.5 # Patty was 4.5 times as heavy as Robbie
    patty_initial_weight = robbie_weight * patty_weight_factor

    # L2
    weight_lost = 235 # lost 235 pounds
    patty_current_weight = patty_initial_weight - weight_lost

    # L3
    weight_difference = patty_current_weight - robbie_weight

    # FA
    answer = weight_difference
    return answer