def solve():
    """Index: 2633.
    Returns: the total number of birds seen from Monday to Wednesday.
    """
    # L1
    birds_monday = 70 # One Monday he sees 70 birds

    # L2
    divisor_tuesday = 2 # half as many birds
    birds_tuesday = birds_monday / divisor_tuesday

    # L3
    additional_birds_wednesday = 8 # 8 more birds
    birds_wednesday = birds_tuesday + additional_birds_wednesday

    # L4
    total_birds = birds_monday + birds_tuesday + birds_wednesday

    # FA
    answer = total_birds
    return answer