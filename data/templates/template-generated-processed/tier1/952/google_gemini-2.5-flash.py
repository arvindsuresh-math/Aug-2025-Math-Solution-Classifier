def solve():
    """Index: 952.
    Returns: the total amount of fish sold in two weeks.
    """
    # L1
    salmon_sold_this_week = 50 # sold 50 kg of salmon
    multiplier_next_week = 3 # three times more
    salmon_sold_next_week = salmon_sold_this_week * multiplier_next_week

    # L2
    total_fish_sold = salmon_sold_this_week + salmon_sold_next_week

    # FA
    answer = total_fish_sold
    return answer