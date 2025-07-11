def solve():
    """Index: 1881.
    Returns: the number of berries Samuel's birds eat in 4 days.
    """
    # L1
    berries_per_bird_per_day = 7 # A bird eats 7 berries a day
    num_days = 4 # in 4 days
    berries_per_bird_in_days = berries_per_bird_per_day * num_days

    # L2
    num_birds = 5 # Samuel has 5 birds
    total_berries = berries_per_bird_in_days * num_birds

    # FA
    answer = total_berries
    return answer