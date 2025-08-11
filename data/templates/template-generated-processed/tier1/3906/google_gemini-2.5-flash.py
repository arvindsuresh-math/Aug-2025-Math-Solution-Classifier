def solve():
    """Index: 3906.
    Returns: the combined weight of Verna and Sherry.
    """
    # L1
    haley_weight = 103 # Haley weighs 103 pounds
    verna_more_than_haley = 17 # Verna weighs 17 pounds more than Haley
    verna_weight = haley_weight + verna_more_than_haley

    # L2
    verna_half_sherry_multiplier = 2 # Verna weighs half as much as Sherry
    sherry_weight = verna_weight * verna_half_sherry_multiplier

    # L3
    total_weight = verna_weight + sherry_weight

    # FA
    answer = total_weight
    return answer