def solve():
    """Index: 55.
    Returns: the percentage of flowers that are not roses.
    """
    # L1
    roses = 25 # 25 roses
    tulips = 40 # 40 tulips
    daisies = 35 # 35 daisies
    total_flowers = roses + tulips + daisies

    # L2
    non_rose_flowers = tulips + daisies

    # L3
    percentage_multiplier = 100 # WK
    percentage_not_roses = (non_rose_flowers / total_flowers) * percentage_multiplier

    # FA
    answer = percentage_not_roses
    return answer