def solve():
    """Index: 55.
    Returns: the percentage of flowers that are not roses.
    """
    # L1
    roses = 25 # 25 roses in a garden
    tulips = 40 # 40 tulips
    daisies = 35 # 35 daisies
    total_flowers = roses + tulips + daisies

    # L2
    not_roses = tulips + daisies

    # L3
    percent_multiplier = 100 # WK
    percent_not_roses = (not_roses / total_flowers) * percent_multiplier

    # FA
    answer = percent_not_roses
    return answer