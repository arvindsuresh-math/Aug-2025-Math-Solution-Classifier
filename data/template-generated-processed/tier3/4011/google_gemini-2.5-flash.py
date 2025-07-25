def solve():
    """Index: 4011.
    Returns: the percentage of the wall taken up by the painting.
    """
    # L1
    painting_length = 2 # 2 foot by 4 foot painting
    painting_width = 4 # 2 foot by 4 foot painting
    painting_area = painting_length * painting_width

    # L2
    wall_length = 5 # 5 foot by 10 foot wall
    wall_width = 10 # 5 foot by 10 foot wall
    wall_area = wall_length * wall_width

    # L3
    percentage_multiplier = 100 # multiply by 100%
    percentage_taken_up = (painting_area / wall_area) * percentage_multiplier

    # FA
    answer = percentage_taken_up
    return answer