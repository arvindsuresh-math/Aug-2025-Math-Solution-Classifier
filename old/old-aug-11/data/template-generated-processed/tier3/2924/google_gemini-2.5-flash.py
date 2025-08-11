def solve():
    """Index: 2924.
    Returns: the percentage of flowers that are blue.
    """
    # L1
    red_flowers = 4 # 4 flowers are red
    white_flowers = 2 # 2 flowers are white
    non_blue_flowers = red_flowers + white_flowers

    # L2
    total_flowers = 10 # Madeline has 10 flowers
    blue_flowers = total_flowers - non_blue_flowers

    # L3
    percentage_multiplier = 100 # WK
    percentage_blue_flowers = (blue_flowers / total_flowers) * percentage_multiplier

    # FA
    answer = percentage_blue_flowers
    return answer