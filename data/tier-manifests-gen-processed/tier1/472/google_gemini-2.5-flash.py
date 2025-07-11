def solve():
    """Index: 472.
    Returns: Lydia's age when she gets to eat an apple from her tree for the first time.
    """
    # L1
    lydia_current_age = 9 # is now 9 years old
    lydia_age_when_planted = 4 # when she was 4 years old
    years_tree_planted = lydia_current_age - lydia_age_when_planted

    # L2
    years_to_bear_fruit_total = 7 # takes 7 years for an apple tree to bear fruit
    years_remaining_to_bear_fruit = years_to_bear_fruit_total - years_tree_planted

    # L3
    lydia_age_when_fruit_bears = lydia_current_age + years_remaining_to_bear_fruit

    # FA
    answer = lydia_age_when_fruit_bears
    return answer