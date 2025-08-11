def solve():
    """Index: 6092.
    Returns: the number of packs of toilet paper Stella bought.
    """
    # L1
    num_bathrooms = 6 # 6 bathrooms
    days_per_week = 7 # every day of the week
    rolls_per_week = num_bathrooms * days_per_week

    # L2
    num_weeks = 4 # After 4 weeks
    total_rolls_needed = rolls_per_week * num_weeks

    # L3
    rolls_per_dozen = 12 # 1 dozen rolls
    packs_of_toilet_paper = total_rolls_needed / rolls_per_dozen

    # FA
    answer = packs_of_toilet_paper
    return answer