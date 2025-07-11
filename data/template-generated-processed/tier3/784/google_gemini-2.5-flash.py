def solve():
    """Index: 784.
    Returns: the difference between the heaviest and lightest pumpkin in pounds.
    """
    # L1
    brad_weight = 54 # Brad entered his pumpkin with a weight of 54 pounds
    half_divisor = 2 # half the weight of Brad's
    jessica_weight = brad_weight / half_divisor

    # L2
    betty_multiplier = 4 # 4 times the amount of Jessica's pumpkin
    betty_weight = betty_multiplier * jessica_weight

    # L3
    difference = betty_weight - jessica_weight

    # FA
    answer = difference
    return answer