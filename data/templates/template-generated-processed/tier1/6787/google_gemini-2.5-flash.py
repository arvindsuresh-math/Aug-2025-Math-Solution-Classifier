def solve():
    """Index: 6787.
    Returns: the total number of fireworks Koby and Cherie have.
    """
    # L1
    koby_sparklers_per_box = 3 # 3 sparklers
    koby_whistlers_per_box = 5 # 5 whistlers
    koby_fireworks_per_box = koby_sparklers_per_box + koby_whistlers_per_box

    # L2
    koby_num_boxes = 2 # 2 boxes of fireworks
    koby_total_fireworks = koby_num_boxes * koby_fireworks_per_box

    # L3
    cherie_sparklers_per_box = 8 # 8 sparklers
    cherie_whistlers_per_box = 9 # 9 whistlers
    cherie_fireworks_per_box = cherie_sparklers_per_box + cherie_whistlers_per_box

    # L4
    total_fireworks = koby_total_fireworks + cherie_fireworks_per_box

    # FA
    answer = total_fireworks
    return answer