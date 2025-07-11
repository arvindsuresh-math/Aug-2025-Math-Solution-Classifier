def solve():
    """Index: 2544.
    Returns: the weight of John's watermelon.
    """
    # L1
    michael_watermelon_weight = 8 # Michael’s largest watermelon weighs 8 pounds
    clay_multiplier = 3 # three times that size
    clay_watermelon_weight = michael_watermelon_weight * clay_multiplier

    # L2
    john_divisor = 2 # half the size of Clay’s
    john_watermelon_weight = clay_watermelon_weight / john_divisor

    # FA
    answer = john_watermelon_weight
    return answer